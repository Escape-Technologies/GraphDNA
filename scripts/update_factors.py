from typing import Generator

import os
import datetime

import requests


def generate_stars_query(
    name: str,
    owner: str,
) -> dict:
    """Generate the query to fetch stars of a certain repo."""

    return {
        'query': f'query {{ repository(owner:"{owner}",name:"{name}") {{ stargazerCount }}}}',
    }


def get_starcount(
    name: str,
    owner: str,
) -> int:
    """Get starcount."""

    token = os.getenv('GITHUB_TOKEN')  # read-only token

    url = 'https://api.github.com/graphql'
    headers = {'Authorization': f'bearer {token}'}
    data = generate_stars_query(name, owner)

    response = requests.post(url, json=data, headers=headers)
    try:
        stars = response.json()['data']['repository']['stargazerCount']
    except Exception as e:
        raise Exception(f'Failed to get starcount for {name} ({e})') from e
    return stars


def valid_query_file(path: str) -> Generator[tuple[str, str], None, None]:
    for file in os.listdir(path):
        if '__' in file or not file.endswith('.py'):
            continue

        with open(f'{path}/{file}', 'r', encoding='utf-8') as f:
            data = f.readline()

        # Not a file, must be an import
        if '/' not in data:
            continue

        yield file, data


def update_queries_starcount(path: str) -> int:
    max_stars = 0

    for file, data in valid_query_file(path):

        print(f'Updating starcount for {file}')

        old_starcount = int(data.split('stars: ')[1].split(',')[0])
        github_directory = data.split(',')[0].split(' ')[-1]
        owner, name = github_directory.split('/')
        starcount = get_starcount(name, owner)

        max_stars = max(starcount, max_stars)
        if starcount == old_starcount:
            continue

        print(f'Updated starcount for {name} ({old_starcount}->{starcount})')

        new_comment = f'# github_directory: {github_directory}, stars: {starcount}, last_update: {datetime.datetime.now().date()}\n'

        with open(f'{path}/{file}', 'r', encoding='utf-8') as f:
            full_file = f.readlines()

        full_file[0] = new_comment
        with open(f'{path}/{file}', 'w', encoding='utf-8') as f:
            f.writelines(full_file)

    # 10% more than the max stars, as some engines are not public
    return max_stars * 1.1


def update_queries_factor(
    path: str,
    max_stars: int,
) -> None:
    for file, data in valid_query_file(path):

        print(f'Updating factor for {file}')

        starcount = int(data.split('stars: ')[1].split(',')[0])
        factor = 0.5 + round(0.5 * starcount / max_stars, 2)

        with open(f'{path}/{file}', 'r', encoding='utf-8') as f:
            full_file = f.readlines()

        for i, line in enumerate(full_file):
            if 'score_factor' in line:
                old_factor = float(line.split('score_factor = ')[1])

                if old_factor == factor:
                    break

                full_file[i] = f'    score_factor = {factor}\n'
                with open(f'{path}/{file}', 'w', encoding='utf-8') as f:
                    f.writelines(full_file)

                print(f'Updated factor for {file} ({factor})')

                break


def update_queries_starcount_factor() -> None:
    directory_path = './graphqldna/heuristics/gql_queries'

    max_stars = update_queries_starcount(directory_path)
    update_queries_factor(directory_path, max_stars)


if __name__ == '__main__':

    assert os.getenv('GITHUB_TOKEN') is not None, 'GITHUB_TOKEN is not set'

    update_queries_starcount_factor()
