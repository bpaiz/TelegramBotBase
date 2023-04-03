#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
DEVELOPER: Byron Paiz.
LAST MODIFICATION: 03.04.2023.
DESCRIPTION: This is the main script for running 'TestBot' on Telegram.
"""

###########################################################################################################################
###################################################### Bot Libraries ######################################################
###########################################################################################################################
#---------------------------------------------------- Other Libraries ----------------------------------------------------#
###########################################################################################################################

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////// Bot handlers //////////////////////////////////////////////////////#
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

###########################################################################################################################
######################################################### Handler #########################################################
###########################################################################################################################
###########################################################################################################################



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#///////////////////////////////////////////////////// Bot functions /////////////////////////////////////////////////////#
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

###########################################################################################################################
###################################################### Main function ######################################################
###########################################################################################################################
def main_function():                                                                                                      #
   updater = Updater(API_KEY, use_context = True)                                                                         #
   dp = updater.dispatcher                                                                                                #
                                                                                                                          #
   dp.add_handler(CommandHandler(START_COMMAND, start_handler))                                                           #
                                                                                                                          #
   updater.start_polling(0)                                                                                               #
   updater.idle()                                                                                                         #
###########################################################################################################################



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#
#//////////////////////////////////////////////////// Bot main-script ////////////////////////////////////////////////////#
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////#

print (CLI_START_MESSAGE)

try:
   while True:
      main_function()
except:
   print ("Unexpected error (main): ", sys.exc_info())
