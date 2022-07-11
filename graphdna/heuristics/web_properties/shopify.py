from graphdna.detectors.checkers import has_json_key
from graphdna.entities.interfaces.dna import IRequest
from graphdna.entities.interfaces.heuristics import IWebProperty


class Shopify(IWebProperty):

    score_factor = 3.0
    requests = [(IRequest('%%base_url%%/products.json', method='GET'), has_json_key('products'))]
