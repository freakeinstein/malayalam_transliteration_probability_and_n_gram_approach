import regex

def read_malayalam(input_file):
	fh=open(input_file,"r")
	s = fh.read() 
	s = regex.sub(r"[^\u0D00-\u0D7F | " "]+", " ", s)
	s = ' '.join(s.split())
	return s