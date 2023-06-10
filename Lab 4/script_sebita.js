// ==UserScript==
// @name         LAB_4_Cripto.tiiny
// @namespace    http://example.com/
// @version      1.0
// @description  try to take over the world!
// @author       You
// @match        https://cripto.tiiny.site/
// @require      https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js

// @grant        none
// ==/UserScript==

(function () {
	"use strict";
	let paragraph = document.querySelector("div.Parrafo");
	let texto = paragraph.innerText;
	//
	let oraciones = texto.split(".");
	let primerosCaracteres = oraciones.map(function (oracion) {
		return oracion.trim().charAt(0);
	});
	let resultado = primerosCaracteres.join("");
	//
	console.log("La llave es: " + resultado); //Indica la llave que se necesita para descifrar
	//
	let mensaje = document.querySelectorAll("div[class^=M]");
	let numero_element = mensaje.length;
	console.log("Los mensajes cifrados son: " + numero_element); //Indica la cantidad de mensajes
	//
	//
	//
	//
	//
	let script = document.createElement("script");
	script.src =
		"https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js";
	script.integrity =
		"sha384-S3wQ/l0OsbJoFeJC81UIr3JOlx/OzNJpRt1bV+yhpWQxPAahfpQtpxBSfn+Isslc";
	script.crossOrigin = "anonymous";
	//
	//
	//
	let llave = CryptoJS.enc.Utf8.parse(resultado); //Se transforma la palabra en una llave
	script.onload = function () {
		//
		for (let i = 0; i < numero_element; i++) {
			let desencriptar = CryptoJS.TripleDES.decrypt(
				mensaje[i].id,
				llave,
				{ mode: CryptoJS.mode.ECB }
			).toString(CryptoJS.enc.Utf8);
			console.log(mensaje[i].id + " " + desencriptar); // Muestra por consola los mensajes y la palabra descifrada
			let resultadoElemento = document.createElement("p");
			resultadoElemento.textContent = desencriptar;
			document.body.appendChild(resultadoElemento);
		}
	};

	document.head.appendChild(script);
})();
