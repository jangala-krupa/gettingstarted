import json
import logging

import tornado.web
#from DfWebhookHandler import dfhandler

class DfWebhookHandler(tornado.web.RequestHandler):
    def get(self):
       # q = self.get_argument('query', 0)
       # logging.info('DfWebhookHandler: request recieved with following params - %s',
                    # q)
        #self.write({"response": q})
        params = json.loads(self.request.body.decode())
        logging.info('DfWebhookHandler: request parameters', params)
        responseObj = {
            "fulfillmentText": " ",
            "fulfillmentMessages": [{"text": {"text": ["krupa-test"]}}],
            "source": ""
        }
        logging.info('DfWebhookHandler: request recieved with following params - %s',
                     responseObj)
        self.write(json.dumps(responseObj))
        

    def post(self):
        params = json.loads(self.request.body.decode())
        logging.info('DfWebhookHandler: request parameters', params)
        responseObj = {
            "fulfillmentText": " ",
            "fulfillmentMessages": [{"text": {"text": ["krupa-test"]}}],
            "source": ""
        }
        logging.info('DfWebhookHandler: request recieved with following params - %s',
                     responseObj)
        self.write(json.dumps(responseObj))

def make_app1():
    return tornado.web.Application([("/", DfWebhookHandler)])
if __name__ == "__main__":
    app = make_app1()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()

