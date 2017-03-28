# -*- coding: utf-8 -*-

#from PyObjCTools import AppHelper
#import AppDelegate
#
#AppHelper.runEventLoop()

import objc
from Cocoa import *
from PyObjCTools import AppHelper

NSWindowDelegate = objc.protocolNamed("NSWindowDelegate")


class AppMenu(NSMenu):
    
    def init(self):
        self = objc.super(AppMenu, self).init()
        if self is None: return None
        a = NSMenu.alloc().init()
        a.addItemWithTitle_action_keyEquivalent_("Quit", "terminate:", "q")
        i = NSMenuItem.alloc().init()
        i.setSubmenu_(a)
        self.addItem_(i)
        return self


class AppWindow(NSWindow, NSWindowDelegate):
    
    def initWithFrame_(self, frame):
        r = frame
        s = NSTitledWindowMask | NSClosableWindowMask | NSMiniaturizableWindowMask | NSResizableWindowMask
        b = NSBackingStoreBuffered
        d = False
        self = objc.super(AppWindow, self).initWithContentRect_styleMask_backing_defer_(r, s, b, d)
        if self is None: return None
        # self.setDelegate_(self)
        self.setReleasedWhenClosed_(False)
        return self
    
    def windowWillClose_(self, sender):
        NSApp.terminate_(sender)


def Window(origin, size):
    w = AppWindow.alloc().initWithFrame_((origin, size))
    return w


class UserInterface(NSObject):
    
    def init(self):
        self = objc.super(UserInterface, self).init()
        if self is None: return None

        appMenu = AppMenu.alloc().init()
        appDelegate = AppDelegate.alloc().init()
        
        window = Window((200,240), (480,270))
        window.setIdentifier_("AppWindow")
        window.setTitle_("Hello")
        
        self.window = window
        self.appMenu = appMenu
        self.appDelegate = appDelegate
        self.appDelegate.window = self.window
        
        return self


class AppDelegate(NSObject):
    
    window = objc.IBOutlet()
    
    def applicationDidFinishLaunching_(self, notification):
        self.window.makeKeyAndOrderFront_(None)
    
    def applicationShouldHandleReopen_hasVisibleWindows_(self, app, flag):
        self.window.makeKeyAndOrderFront_(None)
        return True


if __name__ == "__main__":
    app = NSApplication.sharedApplication()
    top = UserInterface.alloc().init()
    app.setMainMenu_(top.appMenu)
    app.setDelegate_(top.appDelegate)
    app.activateIgnoringOtherApps_(True)
    app.run()
