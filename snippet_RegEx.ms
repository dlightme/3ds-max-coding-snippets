(

fn found searchstr = 
	(
	pattern=@"[D]\d{5}"
	rgx = dotnetObject "System.Text.RegularExpressions.Regex" pattern
	-- C# Regex r = new Regex(pat, RegexOptions.IgnoreCase);
	
	result = rgx.Match searchstr
	return result
	)


input =  "View_09D_D27259x24"
Dplate = found(input)
format "Returned String : % \n" Dplate.Value
	
)