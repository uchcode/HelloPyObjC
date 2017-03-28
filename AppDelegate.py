# -*- coding: utf-8 -*-

import objc
from Cocoa import *

NSApplicationDelegate = objc.protocolNamed('NSApplicationDelegate')

class AppDelegate(NSObject, NSApplicationDelegate):

    window = objc.IBOutlet()

    @objc.IBAction
    def hello_(self, sender):
        print("hello again.")

    def applicationDidFinishLaunching_(self, notification):
        self.window.makeKeyAndOrderFront_(None)

    def applicationShouldHandleReopen_hasVisibleWindows_(self, sender, flag):
        self.window.makeKeyAndOrderFront_(None)
        return True
