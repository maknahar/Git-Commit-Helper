#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import signal
import subprocess
import sys

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

p = subprocess.Popen(['git', 'status'], stdout=subprocess.PIPE)
push = False
last_commit_title = ""
last_commit_desc = ""
description=""

while True:
    new_msg=True
    line = p.stdout.readline()

    #sys.stdout.write(line)
    sys.stdout.flush()
	#if 'Your branch is up-to-date with' in line:
	
	
    if 'modified:' in line or 'new file:' in line or 'renamed:' in line or 'deleted:' in line:
        
        print bcolors.BOLD+bcolors.OKBLUE+line.strip()+bcolors.ENDC
        mfile=''
        
        if 'modified:' in line:
            mfile= line.split("modified:   ",1)[1].strip("\n")
            os.system("git diff "+mfile)
        
        if 'new file:' in line:
            mfile= line.split("new file:   ",1)[1].strip("\n")
            
        if 'renamed:' in line:
            mfile= line.split("renamed:   ",1)[1].strip("\n")
            
        if 'deleted:' in line:
            mfile= line.split("deleted:   ",1)[1].strip("\n")   
            
                 
        commit_msg = raw_input("\nCommit Shortcuts\n a: Added new File <file name>\n b: Bug Fix\n c: Build Issue\n d: Deleted file <file name>\n i: ignore this file from commit\n p: Performance Improvement\n q: same as last file\n r: Renamed file <file name>\n t: Added test case\nEnter Commit Title: ")
        
        if commit_msg.strip()!="i" and commit_msg.strip()!='':
            push = True
            if commit_msg.strip()=="a":
                commit_msg="Added new File: "+ mfile
            if commit_msg.strip()=="b":
                commit_msg="Bug Fix"
            if commit_msg.strip()=="c":
                commit_msg="Build Issue"
            if commit_msg.strip()=="d":
                commit_msg="Deleted File: "+ mfile
            if commit_msg.strip()=="p":
                commit_msg="Performance Improvement"
            if commit_msg.strip()=="q":
                commit_msg=last_commit_title
                description=last_commit_desc
                new_msg=False
            if commit_msg.strip()=="r":
                commit_msg="Renamed file: "+mfile
            if commit_msg.strip()=="t":
                commit_msg="Added test case"

            if new_msg:
                description = raw_input("\nEnter Commit Description(Optional):")
                last_commit_title=commit_msg.strip()
                last_commit_desc=description

            if description == "":
                os.system("git commit "+mfile+ " -m \""+commit_msg+"\"")
            else:
                os.system("git commit "+mfile+ " -m \""+commit_msg+"\""+ " -m \""+description+"\"")


    if line == '':
        break

if push==True:
    print bcolors.OKGREEN+"\n☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺"+bcolors.ENDC
    print bcolors.OKBLUE+ "Finished Committing all new and modified Files."+bcolors.ENDC
    print bcolors.OKGREEN+"☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ ☺ \n"+bcolors.ENDC

print bcolors.BOLD+"Git Status Now:\n"+bcolors.ENDC
os.system("git status")

if push==True:
    confirm = raw_input('\n\nEnter Y to push to remote: ')
    if confirm.strip()=='Y' or confirm.strip()=='y':
        os.system("git push")

p.kill()