'''
idea here is to include PlayFabSettings, set them,
include API.py (or PlayFabSErverAPI.py) and see if you can call a function
out of it.

These test API calls are synchronous and will block the current running python process.
'''

from playfab import *
import PlayFabManualTestSettings

# This needs to be set for the application to work properly.
# This can be found in the GameManger for your Title of the PlayFab website
PlayFabSettings.TitleId = PlayFabManualTestSettings.TitleId
customId = PlayFabManualTestSettings.customId

request = {}

request["CreateAccount"] = True
request["CustomId"] = customId
request["TitleId"] = PlayFabSettings.TitleId
request["LoginTitlePlayerAccountEntity"] = True

def loginCallback(success, fail):
    if fail:
        print(fail)
    else:
        print(success)

PlayFabClientAPI.LoginWithCustomID(request, loginCallback)

def entityTokenCallback(success, fail):
    global EntityKey
    if fail:
        print(fail)
    else:
        EntityKey = success["Entity"]
        print(success)

etRequest = {}
PlayFabEntityAPI.GetEntityToken(etRequest, entityTokenCallback)

def entityObjectCallback(success, fail):
    if fail:
        print(fail)
    else:
        print(success)

# need to add entity id to this request
eoRequest = {}
PlayFabEntityAPI.GetObjects(etRequest, entityObjectCallback)

eoRequest2 = {
    "Entity" : EntityKey
}
PlayFabEntityAPI.GetObjects(eoRequest2, entityObjectCallback)

def titleDataReqCallback(success, fail):
    if fail:
        print(fail)
    else:
        print(success)

try:
    titleDataRequest = {}
    PlayFabServerAPI.GetTitleData(titleDataRequest, titleDataReqCallback)
except PlayFabErrors.PlayFabException as e:
    print("Caught expected error")
    PlayFabSettings.GlobalExceptionLogger(e)

PlayFabSettings.DeveloperSecretKey = PlayFabManualTestSettings.DeveloperSeceretKey

titleDataRequest2 = {}
PlayFabServerAPI.GetTitleData(titleDataRequest, titleDataReqCallback)
