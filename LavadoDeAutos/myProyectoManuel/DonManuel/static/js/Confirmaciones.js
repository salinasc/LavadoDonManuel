function confirmar(id){
    Swal.fire({
        title: '¿Desea eliminar el producto?',
        text: "Esta acción no puede ser revertida",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#dc143c',
        cancelButtonColor: '#292828',
        confirmButtonText: 'Si, borrar producto',
        cancelButtonText: 'Cancelar'
    }).then((result) => {
        if (result.isConfirmed) {
            Swal.fire(
                'Eliminar',
                'Producto eliminado con exito',
                'success'
            ).then(function(){
                window.location.href = "/Eliminar_Producto/"+id+"/";
            })
        }
    })
}
