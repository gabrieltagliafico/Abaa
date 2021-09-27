$(function() {
    $('#datatable').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: { 'action': 'searchdata' },
            dataSrc: ""
        },
        columns: [
            { "data": "id" },
            { "data": "nombre_completo" },
            { "data": "telefono" },
            { "data": "telefono_ad" },
            { "data": "email" },
            { "data": "id_sucursal" },
            { "data": "id_sucursal" },

        ],
        columnDefs: [{
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    var buttons = '<a href="clientes/edit/' + row.id + '/" type="button" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<button type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></button>';
                    return buttons;
                }
            },
            {
                targets: [0],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.id;
                }
            },
            {
                targets: [1],
                class: 'text-center',
                orderable: false,
                render: function(data, type, row) {
                    return row.nombre_completo;
                }
            },
            {
                targets: [2],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.telefono;
                }
            },
            {
                targets: [3],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.telefono_ad;
                }
            },
            {
                targets: [4],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.email;
                }
            },
            {
                targets: [5],
                class: "text-center",
                orderable: false,
                render: function(data, type, row) {
                    return row.id_sucursal;
                }
            },

        ],
        initComplete: function(settings, json) {

        }
    });
});