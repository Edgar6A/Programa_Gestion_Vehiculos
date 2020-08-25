from Vehiculo import *;


# para importsr tienen que estar los dos archivos en la misma carpeta
# luego pones from nombrearchivoClaseImportar import *

opciones = input ("Escribe salir para cerrar el programa, comenzar para agregar un vehiculo:  ");


if opciones == "comenzar":
			tipo = input ("tipo de vehiculo que tienes: ");
			ruedas = input ("de cuantas ruedas es: ");
			color = input ("color del vehiculo: ");
			puertas = input ("numero de puertas: ");
			combustible = input ("combustible que utiliza: ");
			abs = input ("¿ tiene ABS ? ");
			fecha = input ("fecha de fabricacion: ");
			pais = input ("pais donde se fabrico: ");
			pintura = input ("pintura metalizada: ");
			catalizado = input ("esta catalizado: ");
			
			coche = Vehiculo(tipo,ruedas,color,puertas,combustible,abs,fecha,pais,pintura,catalizado);
			
			
			
			lista =[];
			
			
			coche = Vehiculo(tipo,ruedas,color,puertas,combustible,abs,fecha,pais,pintura,catalizado);
			
			lista.append(coche);
		
			
			eleccion = input ("Escribe Salir para cerrar el programa o pulsa 1 para introducir otro vehiculo:  ");
			if eleccion == "salir":
				for x in lista:
					print (x.getTipo() + str(x.getRuedas()) + " Ruedas " + " color " + x.getcolor() + " Puertas: " + str(x.getPuertas()) + " combustible " + x.getCombustible()+ " abs " + x.getAbs() + " año_fab " + x.getFabricacion()+ " pais " + x.getPais() + " Metalizado " + x.getpMetalizada()+ " catalizado " + x.getCatalizado());
			else:
					tipo = input ("tipo de vehiculo que tienes: ");
					ruedas = input ("de cuantas ruedas es: ");
					color = input ("color del vehiculo: ");
					puertas = input ("numero de puertas: ");
					combustible = input ("combustible que utiliza: ");
					abs = input ("¿ tiene ABS ? ");
					fecha = input ("fecha de fabricacion: ");
					pais = input ("pais donde se fabrico: ");
					pintura = input ("pintura metalizada: ");
					catalizado = input ("esta catalizado: ");
					
					coche = Vehiculo(tipo,ruedas,color,puertas,combustible,abs,fecha,pais,pintura,catalizado);
					lista.append(coche);
					
					eleccion = input ("Escribe Salir para cerrar el programa o pulsa 1 para introducir otro vehiculo:  ");
					if eleccion == "salir":
						for x in lista:
							print (x.getTipo() + str(x.getRuedas()) + " Ruedas " + " color " + x.getcolor() + " Puertas: " + str(x.getPuertas()) + " combustible " + x.getCombustible()+ " abs " + x.getAbs() + " año_fab " + x.getFabricacion()+ " pais " + x.getPais() + " Metalizado " + x.getpMetalizada()+ " catalizado " + x.getCatalizado());
					
else:
	print("Debes crear un vehiculo antes de mostrar la lista");
	