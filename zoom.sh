#!/usr/bin/osascript

# usage: zoom <room-number> [room-password] [--name=NAME]

on split(theString, theDelimiter)
	set oldDelimiters to AppleScript's text item delimiters
	set AppleScript's text item delimiters to theDelimiter
	set theArray to every text item of theString
	set AppleScript's text item delimiters to oldDelimiters
	return theArray
end split

on run argv

	set args to {}
	repeat with arg in argv
		 set parts to split(arg, "=")
		 if (count of parts) > 1
		 		if item 1 of parts is "--name"
					set myName to item 2 of parts
				end if
		 else
		   copy item 1 of parts to end of args
		 end if
	end repeat

	try
		myName
	on error
		tell application "System Events"
			set myName to name of current user
		end tell
	end try

	set roomName to item 1 of args
	try
		set roomPassword to item 2 of args
	end try

	log "You are " & myName
	log "Room is " & roomName
	try
		log "Password is " & roomPassword
	end try

	set zoom to "zoom.us"
	tell application zoom to activate
	tell application "System Events"
		repeat until visible of process zoom is false
			log "waiting for zoom process"
			delay 0.2
			set visible of process zoom to false
		end repeat
	end tell

	tell application "System Events"
		tell process zoom

			repeat until window "Join a meeting" exists
				click menu item "Join Meeting..." of menu "Zoom.us" of menu bar 1

				log "waiting for join meeting window"
				delay 0.2
			end repeat

			set joinMeeting to window "Join a meeting"
			set idField to text field 2 of joinMeeting
			set nameField to text field 1 of joinMeeting
			set joinButton to button "Join" of joinMeeting

			set value of idField to roomName
			set value of nameField to myName
			click joinButton

			try
				roomPassword
				repeat until window "Join a Meeting" exists
					log "waiting for password window"
					delay 0.2
				end repeat
				set joinMeeting to window "Join a Meeting"
				set passwordField to text field 1 of group 1 of group 1 of joinMeeting
				set joinButton to button "Join" of group 1 of joinMeeting

				set frontmost to true
				keystroke "."
				set value of passwordField to roomPassword
				click joinButton
			end try

		end tell
	end tell

end run
