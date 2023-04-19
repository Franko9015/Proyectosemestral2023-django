function validaciones(){
    let valida 
    valida=ValidadPassword();
    if (valida===false){
        return false;
    }
    valida=ValidarEdad();
    if (valida==false) {
        return false;
    }
    valida=ValidarLogin();
    if(valida==false){
        return false;
    }
    return true;
}



function ValidadPassword() {
    var pass1=document.getElementById("txtPass1").value;
    var pass2=document.getElementById("txtPass2").value;
    if (pass1==pass2) {
        //alert('OK');
        console.log('OK')
        let largo= pass1.length;
        let largo2=pass2.length ;
        if (largo<5) {
            Swal.fire({
               icon: 'error',
                title: 'Oops...',
              text: 'Largo Pass 1 incorrecto'});
            return false;
        }
        if(largo2<5){
            Swal.fire({ icon: 'error',
               title: 'Oops...',
               text: 'Largo Pass 2 incorrecto'});
            return false;
        }
        return true;
    }else{
        Swal.fire({icon: 'error',
            title: 'Oops...',
            text: 'Pass no son iguales'});
        //alert('Pass no son iguales');
        return false;
    }
}

function ValidarEdad(){
    let mi_fecha= document.getElementById("datfecha").value;
    let fecha_actual=new Date();
    console.log('Mi Fecha:'+mi_fecha);
    console.log('Fecha Actual:'+fecha_actual);
    let ano=mi_fecha.slice(0,4);
    let mes=mi_fecha.slice(5,7);
    let dia=mi_fecha.slice(8,10);
    let fecha_comparar=new Date (ano,(mes-1),dia);
    if (fecha_comparar>fecha_actual){
        alert('fecha ingresada mayor a la actual'); 
        return false;
    }
    let dia_mili = 1000*60*60*24;
    console.log('dia en milisegundos:'+dia_mili);
    let dias_vividos=(fecha_actual.getTime()-fecha_comparar.getTime())/dia_mili;
    console.log('Dias Vividos'+ Math.trunc( dias_vividos));
    let anos_vividos= Math.trunc (dias_vividos/365);
    console.log('Años:'+anos_vividos);
if (anos_vividos<18){
    Swal.fire({icon: 'error',
    title: 'Error',
    text: 'Para Registrarte, debes ser mayor a 18 años'});
    //alert('Para Registrarte, debes ser mayor a 18 años');
    return false
}
return true;
}

  function ValidarLogin() {
    // Obtiene los valores de entrada del usuario
    var username = document.getElementById("Ejemplo1").value;
    var password = document.getElementById("Ejemplo2").value;

    // Verifica si el nombre de usuario y la contraseña son válidos
    if (username == "" || password == "") {
        Swal.fire({icon: 'error',
        title: 'Error',
        text: 'Porfavor Ingrese Su Correo Y Contraseña'})  
    //alert("Por favor ingrese su nombre de usuario y contraseña.");
      return false;
    }

    // Si los valores son válidos, permite que el usuario inicie sesión
    return true;
  }


