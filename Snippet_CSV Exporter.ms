--txt = "insert your text"
f = (createFile "C://Users/w.haak/Desktop/maxscript/consetned.csv")


consentedlist = #()

for task in objects where SuperClassOf task== GeometryClass do
	(
		OS_E = GetUserProp task "OS_Easting" as string
		OS_N = GetUserProp task "OS_Northing" as string
		format "%,%,%\n" task.name OS_E OS_N to:f
	)

---- Output formatting
		--format "%,%,%,%,%,%,%,%\n" cName CamE CamN cam.pos[3] getZ distance2D iOSE iOSN
	
close f