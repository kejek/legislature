__author__ = 'cla283'
class XUACompatibleMiddleware(object):
    """
    Add a X-UA-Compatible header to the response
    This header tells to Internet Explorer to render page with latest
    possible version or to use chrome frame if it is installed.
    """
    def process_response(self, request, response):
        response['X-UA-Compatible'] = 'IE=edge,chrome=1'
        return response
