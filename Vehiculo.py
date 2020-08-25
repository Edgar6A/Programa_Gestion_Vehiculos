class Vehiculo:
	tipo="";
	ruedas=1;
	color="";
	puertas=0;
	combustible="";
	abs=False;
	fabricacion="";
	pais="";
	pMetalizada=False
	catalizado=False;
	
	def __init__(self,tip,rue,col,puerta,comb,ab,fech,ps,metal,cataliz):
		self.tipo=tip;
		self.ruedas=rue;
		self.color=col;
		self.puertas=puerta;
		self.combustible=comb;
		self.abs=ab;
		self.fabricacion=fech;
		self.pais=ps;
		self.pMetalizada=metal;
		self.catalizado=cataliz;
		
		
	
	def getTipo(self):
		return self.tipo;
	
	def getRuedas(self):
		return self.ruedas;
	
	def getcolor(self):
		return self.color;
	
	def getPuertas(self):
		return self.puertas;
		
	def getCombustible(self):
		return self.combustible;
		
	def getAbs(self):
		return self.abs;

		
	def getFabricacion(self):
		return self.fabricacion;
		
	def getPais(self):
		return self.pais;
		
	def getpMetalizada(self):
		return self.pMetalizada;
		
	def getCatalizado(self):
		return self.catalizado;
	
	
	
	
