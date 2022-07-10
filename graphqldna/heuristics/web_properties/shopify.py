from graphqldna.entities.interfaces.dna import IRequest
from graphqldna.entities.interfaces.heuristics import IWebProperty


class Shopify(IWebProperty):

    score_factor = 3.0
    requests = [IRequest('%%base_url%%/products.json', method='GET')]
