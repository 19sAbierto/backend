import random


tokens = ['que', 'por', 'una', 'con', 'para', 'pero', 'bien', 'eso', 'del', 'como', 'todo', 'muy', 'esto', 'ahora', 'esta', 'hay', 'estoy', 'algo', 'tengo', 'nada', 'cuando', 'quiero', 'este', 'tiene', 'puedo', 'bueno', 'soy', 'era', 'ser', 'vez', 'hacer', 'ella', 'son', 'fue', 'usted', 'puede', 'ese', 'voy', 'casa', 'creo', 'porque', 'tan', 'favor', 'hola', 'nunca', 'verdad', 'mucho', 'estaba', 'tiempo', 'esa', 'mejor', 'hombre', 'hace', 'vida', 'sin', 'ver', 'hasta', 'siento', 'decir', 'sobre', 'uno', 'noche', 'poco', 'otra', 'quiere', 'solo', 'nadie', 'padre', 'gente', 'parece', 'dinero', 'estar', 'hecho', 'mismo', 'sea', 'mira', 'pasa', 'dijo', 'claro', 'han', 'otro', 'desde', 'mundo', 'hablar', 'tal', 'sabe', 'donde', 'fuera', 'hijo', 'seguro', 'mujer', 'amigo', 'madre', 'cosa', 'lugar', 'dice', 'gusta', 'gran', 'mierda', 'espera', 'hoy', 'tener', 'ven', 'buena', 'estado', 'nuevo', 'luego', 'dije', 'sido', 'debe', 'tipo', 'buen', 'mal', 'nombre', 'toda', 'amor', 'visto', 'tarde', 'parte', 'tienen', 'tanto', 'cada', 'hora', 'haber', 'dicho', 'quien', 'oye', 'saber', 'entre', 'vaya', 'cierto', 'debo', 'alguna', 'veo', 'idea', 'chica', 'hizo', 'serio', 'cabeza', 'digo', 'van', 'pasado', 'salir', 'cuenta', 'vale', 'mes', 'pueden', 'muerto', 'viejo', 'lado', 'suerte', 'miedo', 'contra', 'puerta', 'pronto', 'casi', 'nueva', 'espero', 'agua', 'chico', 'venga', 'camino', 'hacia', 'dentro', 'ciudad', 'viene', 'deja', 'forma', 'volver', 'feliz', 'guerra', 'caso', 'esposa', 'mano', 'hice', 'muerte', 'loco', 'toma', 'pasar', 'iba', 'semana', 'jefe', 'venir', 'ayuda', 'vete', 'arriba', 'hija', 'sra', 'tierra', 'manera', 'fin', 'cara', 'grande', 'cinco', 'llama', 'hey', 'habla', 'bajo', 'poder', 'aunque', 'cerca', 'cree', 'dame', 'sigue', 'auto', 'cuatro', 'dejar', 'igual', 'hago', 'listo', 'clase', 'llegar', 'doctor', 'tomar', 'vivir', 'joven', 'haya', 'abajo', 'primer', 'genial', 'justo', 'pensar', 'misma', 'puta', 'comer', 'fui', 'entrar', 'fuerte', 'srta', 'morir', 'basta', 'dar', 'amo', 'dicen', 'pueda', 'punto', 'vino', 'final', 'pueblo', 'haga', 'sangre', 'coche', 'juego', 'cuerpo', 'mayor', 'eran', 'queda', 'paz', 'dime', 'vuelta', 'tenido', 'sola', 'hacen', 'ido', 'culpa', 'malo', 'comida', 'saben', 'alto', 'dormir', 'fiesta', 'cama', 'medio', 'diga', 'trata', 'equipo', 'cuanto', 'idiota', 'luz', 'tuve', 'matar', 'verte', 'venido', 'fueron', 'tenga', 'cuarto', 'cielo', 'vivo', 'falta', 'creer', 'john', 'pienso', 'aqui', 'marido', 'perro', 'calle', 'rey', 'lista', 'carajo', 'par', 'fuego', 'seguir', 'mucha', 'paso', 'afuera', 'dio', 'piensa', 'ello', 'lleva', 'estuvo', 'sitio', 'libro', 'vuelve', 'minuto', 'arma', 'viaje', 'jugar', 'diez', 'dado', 'mil', 'gusto', 'peor', 'irme', 'jack', 'orden', 'cambio', 'pobre', 'ropa', 'sino', 'modo', 'ocurre', 'libre', 'anoche', 'acerca', 'negro', 'buscar', 'segura', 'frente', 'puesto', 'asunto', 'duro', 'sucede', 'llamar', 'boca', 'mire', 'encima', 'mala', 'llevar', 'cual', 'odio', 'deben', 'resto', 'llamo', 'perder', 'york', 'ayudar', 'tuvo', 'largo', 'pena', 'ayer', 'dile', 'prueba', 'siendo', 'bonito', 'haz', 'real', 'tonto', 'aire', 'conoce', 'fuerza', 'carta', 'trato', 'plan', 'verlo', 'hambre', 'vuelto', 'campo', 'acaba', 'vive', 'barco', 'hotel', 'poner', 'grupo', 'sol', 'tuyo', 'pase', 'joe', 'voz', 'usar', 'placer', 'blanco', 'estuve', 'pie', 'anda', 'espere', 'edad', 'tren', 'prisa', 'vista', 'gustan', 'pagar', 'george', 'futuro', 'siente', 'quiera', 'loca', 'frank', 'sal', 'raro', 'viste', 'novia', 'amiga', 'dan', 'llevo', 'pelo', 'the', 'error', 'propia', 'ganar', 'ley', 'dolor', 'oro', 'ten', 'deseo', 'mente', 'darle', 'acabo', 'david', 'suena', 'mitad', 'vio', 'mesa', 'entra', 'tom', 'mar', 'siete', 'sexo', 'amable', 'traje', 'alma', 'dale', 'san', 'cena', 'propio', 'culo', 'asi', 'sam', 'temo', 'abre', 'fuiste', 'media', 'foto', 'centro', 'miren', 'bonita', 'ante', 'pude', 'luna', 'doy', 'normal', 'junto', 'tienda', 'abuela', 'vine', 'sale', 'honor', 'hablo', 'vieja', 'papel', 'dejado', 'juro', 'dulce', 'sentir', 'caja', 'ocho', 'perra', 'trae', 'paul', 'vienen', 'sean', 'llega', 'abuelo', 'linda', 'hubo', 'lindo', 'hazlo', 'busca', 'don', 'baja', 'pudo', 'salud', 'cita', 'agente', 'regalo', 'carne', 'piso', 'esposo', 'harry', 'deje', 'tuya', 'beber', 'calma', 'salvo', 'basura', 'suelo', 'rato', 'bailar', 'triste', 'nena', 'banco', 'supone', 'existe', 'alegro', 'santo', 'novio', 'broma', 'radio', 'vuelva', 'cenar', 'corre', 'muerta', 'bob', 'diablo', 'norte', 'sala', 'ataque', 'baile', 'club', 'duda', 'boda', 'quise', 'reina', 'sur', 'pone', 'escena', 'mike', 'obra', 'aquel', 'creen', 'aun', 'mary', 'viva', 'bill', 'llave', 'simple', 'irse', 'leer', 'joder', 'cocina', 'corte', 'locura', 'cine', 'verla', 'duele', 'tocar', 'mirar', 'verme', 'ben', 'suyo', 'causa', 'pelea', 'jim', 'fondo', 'acaso', 'vuelvo', 'toca', 'tome', 'hogar', 'rico', 'trago', 'capaz', 'cargo', 'lleno', 'bar', 'vayan', 'humano', 'ojo', 'lee', 'zona', 'henry', 'sacar', 'jimmy', 'tema', 'matado', 'johnny', 'pido', 'cierra', 'peter', 'calor', 'color', 'vea', 'valor', 'azul', 'arte', 'pedir', 'puso', 'llaman', 'oiga', 'juez', 'precio', 'rojo', 'hagan', 'verano', 'podido', 'isla', 'darme', 'vengan', 'parar', 'banda', 'marcha', 'crimen', 'dejo', 'ama', 'debajo', 'come', 'contar', 'ganado', 'juicio', 'estilo', 'sepa', 'viendo', 'salida', 'alegra', 'darte', 'quedan', 'nota', 'nave', 'base', 'sube', 'vuelo', 'golpe', 'viento', 'desea', 'beso', 'ruido', 'salga', 'brazo', 'quedar', 'irte', 'casado', 'llegue', 'copa', 'menudo', 'partir', 'visita', 'alta', 'abrir', 'tony', 'nueve', 'bomba', 'bolsa', 'santa', 'pan', 'piel', 'usa', 'exacto', 'cuello', 'larga', 'salvar', 'sirve', 'llena', 'subir', 'blanca', 'steve', 'dama', 'suya', 'doble', 'vengo', 'bosque', 'max', 'taxi', 'volar', 'debido', 'leche', 'nick', 'tanta', 'correr', 'eddie', 'billy', 'muere', 'acabar', 'probar', 'pedido', 'dieron', 'salido', 'llame', 'you', 'tratar', 'sigo', 'oeste', 'traer', 'tiro', 'cerdo', 'gato', 'reloj', 'hable', 'bella', 'teatro', 'papi', 'hielo', 'cantar', 'bajar', 'pelear', 'paga', 'lucha', 'cabo', 'verde', 'pareja', 'nariz', 'caer', 'herido', 'pista', 'bebe', 'sonido', 'evitar', 'llorar', 'vender', 'nivel', 'dando', 'gay', 'roma', 'papa', 'pierna', 'ray', 'enorme', 'mando', 'ponte', 'alex', 'pesar', 'animal', 'luchar', 'date', 'tomado', 'estan', 'gana', 'robert', 'motivo', 'puente', 'cuento', 'cuesta', 'espada', 'silla', 'bobby', 'pared', 'prensa', 'trampa', 'grave', 'siga', 'danny', 'alguno', 'anillo', 'total', 'tommy', 'piedra', 'tengan', 'oigan', 'ahi', 'playa', 'costa', 'quede', 'paseo', 'pon', 'negra', 'tonta', 'imagen', 'show', 'lleve', 'sarah', 'llevan', 'red', 'dejen', 'and', 'turno', 'yendo', 'ponga', 'pasada', 'mata', 'gracia', 'guapa', 'querer', 'deber', 'trajo', 'primo', 'supe', 'sir', 'diario', 'quedo', 'martin', 'jake', 'www', 'mami', 'lluvia', 'cien', 'lengua', 'china', 'ayude', 'quiso', 'puse', 'pago', 'mirada', 'quieto', 'dura', 'humana', 'humor', 'jane', 'entero', 'roja', 'larry', 'echar', 'roto', 'actuar', 'mark', 'polvo', 'coger', 'bravo', 'europa', 'verle', 'toque', 'amante', 'saca', 'rosa', 'peso', 'carga', 'acto', 'robar', 'bote', 'huele', 'gordo', 'puto', 'anna', 'cerrar', 'gloria', 'oscuro', 'cuidar', 'dedo', 'ruego', 'tumba', 'coge', 'metido', 'limpio', 'jerry', 'guapo', 'uso', 'duerme', 'dave', 'dia', 'parque', 'cambia', 'cinta', 'famoso', 'siguen', 'pide', 'abrigo', 'diste', 'menor', 'genio', 'oigo', 'pongo', 'lago', 'unidad', 'efecto', 'robo', 'empleo', 'pollo', 'whisky', 'jodido', 'cae', 'nieve', 'busco', 'riesgo', 'sucio', 'walter', 'fuese', 'salgan', 'carro', 'rostro', 'pedazo', 'cola', 'marca', 'hablan', 'tesoro', 'camisa']


def diceware(n, sep='.'):
    return sep.join(random.sample(tokens, n))
