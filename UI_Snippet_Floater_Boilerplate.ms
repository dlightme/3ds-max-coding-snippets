(

rollout myrollout "Rollout Title"
(
	-- some UI stuff
	button mybutton "press me" tooltip:"this is a duffer"
	
	-- some actions and functions
	on mybutton pressed do (messageBox "You pressed the button")
	
)

--- Create Floater---
try (closeRolloutFloater MyFloater)catch()
MyFloater = newRolloutFloater "Floater Title" 300 350
--- Add default Rollouts---
addrollout myrollout MyFloater rolledUp:false

)