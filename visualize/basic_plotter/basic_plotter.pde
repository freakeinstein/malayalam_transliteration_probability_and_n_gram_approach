ArrayList<XY> coords;
float max_x = 1;
float max_y = 1;

int iterator = 0;
float _x = 0;
float _y = 0;
float dx;
float dy;

boolean pause = false;

void setup(){
  size(500,500);
  surface.setResizable(true);
  coords = new ArrayList<XY>();
  max_y = readInput("../../bigram_mal_corpus.txt");
  //print(max_y);
  max_x = coords.size();
  stroke(0);
  //background(255);
  frameRate(100);
}

void draw(){
  dx = width/max_x;
  dy = height/max_y;
  //print(max_x,max_y,dx,dy);
  
  for(int i = 1; i<4 ;i++){
    stroke(10,200,50);
    line(0,height/4*i,width,height/4*i);
    stroke(200,20,50);
    line(width/4*i,0,width/4*i,height);
  }
    _y = dy*(coords.get(iterator).getY());
    stroke(0);
    line(_x,height,_x,height - _y);
    _x += dx;
    
  
  
  iterator++;
  if(iterator >= max_x) { iterator = 0; _x = 0; }
}

int readInput(String in_file){
  BufferedReader reader;
  int mx_y = 1;
  reader = createReader(in_file);
  while(true){
    String line;
    try {
      line = reader.readLine();
    } catch (Exception e) {
      e.printStackTrace();
      line = null;
    }
    if (line == null) {
      // Stop reading because of an error or file is empty
      break;  
    } else {
      String[] pieces = split(line, ':');
      if(pieces.length <= 1){
        mx_y = Integer.parseInt(split(line, '#')[1]);
      }else{
        String x = pieces[0];
        float y = float(pieces[1]);
        // Operations to smooth out the graph outliers
        y = 1+log(y);
        y*=10000; 
        // End of smoothening
        //print(x);
        coords.add(new XY(x,(int)y));
      }
    }
  }
  return mx_y;
}

void mousePressed(){
  background(255);
  pause = !pause;
  if(pause) noLoop();
  else loop();
}