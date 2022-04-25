# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:         sfp_showStatusCode
# Purpose:      View status code of diferrent web.
#
# Author:      Pablo Escalante Romero <pabloescalanteromero@gmail.com>
#
# Created:     25/04/2022
# Copyright:   (c) Pablo Escalante Romero 2023
# Licence:     GPL
# -------------------------------------------------------------------------------


from spiderfoot import SpiderFootEvent, SpiderFootPlugin
import subprocess

class sfp_showStatusCode(SpiderFootPlugin):

    meta = {
        'name': "show Status Code",
        'summary': "View status code of diferrent web",
        'flags': [""],
        'useCases': [""],
        'categories': ["Passive DNS"] #LO cambiamos luego
    }

    # Default options
    opts = {
    }

    # Option descriptions
    optdescs = {
    }

    results = None

    def setup(self, sfc, userOpts=dict()):
        self.sf = sfc
        self.results = self.tempStorage()

        for opt in list(userOpts.keys()):
            self.opts[opt] = userOpts[opt]

    # What events is this module interested in for input
    def watchedEvents(self):
        return ["DOMAIN_NAME"]

    # What events this module produces
    # This is to support the end user in selecting modules based on events
    # produced.
    def producedEvents(self):
        return ["HTTP_CODE"]

    # Handle events sent to this module
    def handleEvent(self, event):
        eventName = event.eventType
        srcModuleName = event.module
        eventData = event.data

        if eventData in self.results:
            return

        self.results[eventData] = True

        self.sf.debug(f"Received event, {eventName}, from {srcModuleName}")

        try:
            self.sf.debug(f"We use the data: {eventData}")
            print(f"We use the data: {eventData}")

            ########################
            # Insert here the code #
            ########################

            #Ejecutamos el comando
            data = subprocess.run('curl -I '+eventData,shell=True, text=True, capture_output=True)
            out = data.stdout

            #Separamos el texto con espacios
            outServer = out.split(" ")

            #Seleccion el codigo de estado
            server = outServer[1]

            ########################

            if not server:
                self.sf.error("Unable to perform <ACTION MODULE> on " + eventData)
                return
        except Exception as e:
            self.sf.error("Unable to perform the <ACTION MODULE> on " + eventData + ": " + str(e))
            return

        evt = SpiderFootEvent(eventName, server, self.__name__, event)
        self.notifyListeners(evt)

# End of sfp_showStatusCode