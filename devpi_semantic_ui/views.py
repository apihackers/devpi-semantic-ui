from pyramid.view import view_config

from devpi_server.views import apireturn
from devpi_web.views import SearchView


def clean_item(item):
    if 'words' in item:
        item['words'] = list(item['words'])
    for hit in item.get('sub_hits', []):
        clean_item(hit)

def emptyresult():
    return {'items': [], 'info': {'pagecount': 0, 'total': 0}}


@view_config(route_name='searchapi',
             accept='application/json',
             content_type='application/json')
def search(request):
    search_view = SearchView(request)
    result = search_view.result or emptyresult()
    result['query'] = search_view.params['query'],
    # transform frozenset into list
    for item in result['items']:
        clean_item(item)
    apireturn(200, type="search_result", result=result)
