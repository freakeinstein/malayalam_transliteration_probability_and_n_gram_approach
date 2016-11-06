/* Author: http://nandakumar.co.in/apps/parayumpole.html */

// Setting up replace content
//പുനസ്താപിക്കുവാനുള്ള അക്ഷരങ്ങള്‍ ശരിയാക്കി വയ്ക്കുന്നു. 
replace2=["aa","ee","oo","ai","ou"];
replace2new=["A","^","U","I","<"];
replace3=[" aa"," ee"," oo"," ou"," am"];
replace3new=[" A"," ^"," U"," <"," `"];
vow=["a","A","i","^","u","U","~","e","E","I","o","O","<"];
vowml=["അ","ആ","ഇ","ഈ","ഉ","ഊ","ഋ","എ","ഏ","ഐ","ഒ","ഓ","ഔ"];
cons=["k","K","g","G","c","C","j","J","t","T","d","D","N","n","p","P","b","B","m","y","r","l","v","S","s","h","L","Z","R","f","M",".",",","'","\"",";",":","?","!","/","-","_","+","=","(",")","&","%","@","$","1","2","3","4","5","6","7","8","9","0"];
consml=["ക","ഖ","ഗ","ഘ","ച","ഛ","ജ","ഝ","ട","ഠ","ദ","ഡ","ണ","ന","പ","ഫ","ബ","ഭ","മ","യ","ര","ല","വ","ശ","സ","ഹ","ള","ഴ","റ","ഫ","മ്മ",".",",","'","\"",";",":","?","!","ഽ","-","_","+","=","(",")","&","%","@","ഃ","൧","൨","൩","൪","൫","൬","൭","൮","൯","൦"];
symbols=["a","A","i","^","u","U","~","e","E","I","o","O","<","`","\\"];
symml=["","ാ","ി","ീ","ു","ൂ","ൃ","െ","േ","ൈ","ൊ","ോ","ൗ","ം","്‍"];
hchar=["k","g","N","c","j","n","t","T","d","D","p","b","s","z"];
hcharml=["ഖ","ഘ","ങ","ച","ഝ","ഞ","ത","ഥ","ധ","ഢ","ഫ","ഭ","ഷ","ഴ"];

special1 = ["n", "n", "m"];
special2 = ["g", "j", "p"];
special3 = ["ങ", "ഞ", "മ്പ"];

// Method to convert mangleesh chars to malayalam chars (parameter:mangleesh return: malayalam)
// മങ്ക്ലീഷ് അക്ഷരങ്ങളെ ഇങ്ക്ലീഷിലേക്ക് ആക്കാനുള്ള വഴി. 
function get_ml(en)
{
	//en  = "|" + document.getElementById("ta_in").value;
	en  = "|" + en;
	//alert(en);
	ml = "";
	n = 0;
	disabled = false;

	while(n < en.length)
	{
		var prv_ch ="", nxt_ch="", later_ch="";
		ch = en[n];

		if(ch == "{")
		{
			disabled = true;
			ch = "";
		}

		if(ch == "}") disabled = false;

		if(disabled) // {english}
		{
			n++;
		}
		else
		{
			if(n > 0)                prv_ch = en[n - 1];
			if(n < (en.length - 1)) nxt_ch = en[n + 1];
			if(n < (en.length - 2)) later_ch = en[n + 2];

			for(i in replace3)
			{
				if(replace3[i] == ch + nxt_ch + later_ch)
				{
					en = en.slice(0, n+1) + replace3new[i] + en.slice(n+3, en.length);
				}
			}

			for(i in replace2)
			{
				if(replace2[i] == nxt_ch + later_ch)
				{
					en = en.slice(0, n+1) + replace2new[i] + en.slice(n+3, en.length);
				}
			}

			done = false;
			n++;
		}
	}

	n = 0;
	disabled = false;

	while(n < en.length)
	{
		var prv_ch ="", nxt_ch="", later_ch="";
		ch = en[n];

		if(ch == "{")
		{
			disabled = true;
			ch = "";
		}

		if(ch == "}") disabled = false;
		
		if(disabled) // {english}
		{
			ml += ch;
			n++;
		}
		else
		{
			if(n > 0)                prv_ch = en[n - 1];
			if(n < (en.length - 1)) nxt_ch = en[n + 1];
			if(n < (en.length - 2)) later_ch = en[n + 2];


			done = false;

			if(ch == "\n")
			{
				en = en.slice(0, n) + "|\n|" + en.slice(n+1, en.length);
				ml += "\n";
				n++;
			}

			if(done == false)
			{
				if(ch == " " || ch == "|")
				{
					connector = "";
					if(ch == " ") connector=" ";

					for(vi in vow)
					{
						if(vow[vi] == nxt_ch)
						{
							ml += (connector + vowml[vi]);
							done = true;
							n += 2;
						}
					}

					if(done == false)
					{
						ml += connector;
						done = true;
						n++;
					}

				}
			}

	// Some special cases  
			for(i in special1)
			{
				if(done == false && ch == special1[i] && nxt_ch == special2[i])
				{
					buff = "്";
					for(si in symbols)
					{
						if(symbols[si] == later_ch) buff = symml[si];
					}
					ml += (special3[i] + buff);
					n += 2;
					done = true;
				}
			}

	// m
			if(done == false && ch == "m")
			{					
				if(nxt_ch != "m" && nxt_ch != "a" && nxt_ch != "A" && nxt_ch != "i" && nxt_ch != "^" && nxt_ch != "u" && nxt_ch != "U" && nxt_ch != "~" && nxt_ch != "e" && nxt_ch != "E" && nxt_ch != "I" && nxt_ch != "o" && nxt_ch != "O" && nxt_ch != "<")
				{
					buff="്";

					for(si in symbols)
					{
						if(symbols[si] == prv_ch) buff = symml[si];
					}

					if(buff != "്")
					{
						ml += "ം";
						n++;
						done = true;
					}
					else
					{
						done = false;
					}
				}
			}

	// h
			if(done == false && nxt_ch == "h")
			{
				for(hi in hchar)
				{
					if(hchar[hi] == ch)
					{
						buff = "്";

						for(si in symbols)
						{
							if(symbols[si] == later_ch) buff = symml[si];
						}

						ml += (hcharml[hi] + buff);
						n += 2;
						done = true;
					}
				}
			}

	// not h
			if(done == false && nxt_ch != "h")
			{	
				for(ci in cons)
				{
					if(cons[ci] == ch)
					{

						if(ci < 30)
						{
							buff="്"; // items after 37 are with 'a' in built.
						}
						else
						{
							buff="";
						}

						symn = 0;

						for(si in symbols)
						{
							if(symbols[si] == nxt_ch) buff = symml[si];
						}
	
						ml += (consml[ci] + buff);
					}
				}

				n++;
				done = true;
			}

			if(done == false)
			{
				n++; // Not a good way! DONE shouldn't be FALSE here.
			}
		}

	
	}
	
	return ml;
};

