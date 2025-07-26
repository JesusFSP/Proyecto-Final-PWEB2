var app = angular.module('SazonPeruanaApp', []);

app.controller('ReservaController', function ($scope, $http) {
    $scope.reserva = {};

    $scope.formatDate = function (dateString) {
        if (!dateString) return null;
        const date = new Date(dateString);
        return date.toISOString().split('T')[0];
    };

    $scope.formatTime = function (timeString) {
        if (!timeString) return null;
        const parts = timeString.split(':');
        const hours = parts[0].padStart(2, '0');
        const minutes = parts[1].padStart(2, '0');
        return `${hours}:${minutes}:00`;
    };

    $scope.submitForm = function () {
        const datosEnvio = {
            nombre_cliente: $scope.reserva.nombre_cliente,
            correo_cliente: $scope.reserva.correo_cliente,
            telefono_cliente: $scope.reserva.telefono_cliente,
            fecha_reserva: $scope.formatDate($scope.reserva.fecha_reserva),
            hora_reserva: $scope.formatTime($scope.reserva.hora_reserva),
            cantidad_personas: parseInt($scope.reserva.cantidad_personas)
        };

        if ($scope.reservaForm.$valid) {
            $http.post('/api/reservas/', $scope.reserva)
                .then(function(response) {
                    alert('¡Reserva confirmada! Se ha enviado un correo de confirmación');
                    $window.location.href = '/';  // Redirige a la página principal
                })
                .catch(function(error) {
                    console.error("Error completo:", error);
                    alert('Error: ' + (error.data.detail || JSON.stringify(error.data)));
                });
        }

        console.log("Datos a enviar:", datosEnvio);

        $http.post('/api/reservas/', datosEnvio, {
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            }
        }).then(function (response) {
            alert('¡Reserva creada con éxito!');
            $scope.reserva = {}; // Limpiar formulario
        }).catch(function (error) {
            console.error("Error completo:", error);
            alert('Error al crear reserva: ' +
                (error.data.detail || JSON.stringify(error.data)));
        });
    };

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});