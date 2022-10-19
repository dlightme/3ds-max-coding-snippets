(
a= 104.452
b = 505.52
c = 324.499

fn round toround ex = 
(
	modulo = mod toround ex
	adjmod = 0.5 * ex
	if modulo < adjmod then 
		(
		toround = toround - modulo
		return toround
		)
	else
		(
		print (modulo)
		print (ex)			
		toround = toround - modulo + ex
		return toround
		)
)

print ("A " + (round a 10) as string)
print ("B " + (round b 10) as string)
print ("C " + (round c 10) as string)
)