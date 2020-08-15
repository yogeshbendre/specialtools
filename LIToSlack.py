from flask import Flask, request
import json
import subprocess as sp
#from postnote import postAlert
import pandas as pd

import slack
from slack import WebClient
import json

def postAlert(mychannel, myalertname, mymessage):

    print("Channel: "+mychannel)
    print("Message: "+mymessage)
    mytoken=json.load(open("bot_token.json","r"))
    slack_token = mytoken["token"]#"xoxb-2154537752-1082420677300-Oodl4DjG1AY3gbo5Z5whO32e"
    client = WebClient(slack_token, timeout=30)

    order_dm = client.chat_postMessage(
                       as_user=True,
                       channel=mychannel,
                        text=myalertname,
                       attachments=[
                        {
                            "text": mymessage
                        }
                    ])
    print(order_dm)





app = Flask('WebappReceiver')

def buildmessage(mydata):
    try:
        mymsg = mydata["AlertName"]+"\n\n"
        mydatadict = {}
        for m in mydata["messages"]:
            for f in m["fields"]:
                if f["name"]=='count':
                    continue
                mymsg = mymsg + f["name"] +" = " + f["content"] + ","
                if f["name"] not in mydata.keys():
                    mydatadict[f["name"]] = []
                mydatadict[f["name"]].append(f["content"])
            mymsg = mymsg + "\n"

        mymsg = mymsg + "\n----------------------------------------------------------"
        df = pd.DataFrame(mydatadict)
        print(df)
        return(df.to_string())
    except Exception as e:
        print(str(e))
        return None


try:
    print("starting app")

    @app.route('/lialert', methods=['POST'])
    def lialert():
        print("Sending Message")
        myrequest = request.get_json()
        print("Data:\n")
        print(myrequest)
        msg = buildmessage(myrequest)
        msg = "Details:\n" + msg
        print("Message to be sent")
        print(msg)
        if msg is not None:
            postAlert("#large_hedron_collider", myrequest["AlertName"], msg)
            print("Posted")
        return('Posted: ' + str(myrequest))


    @app.route('/', methods=['GET'])
    def button2():
        print("getting json data")
        return 'Hello world'

except Exception as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print("Got an error: {e.response['error']}")


if __name__ == '__main__':
    app.run('0.0.0.0', 7010, debug=False)
