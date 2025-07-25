var app = angular.module('SazonPeruanaApp', []);

app.controller('ReservaController', function($scope, $http) {
    $scope.reserva = {};
    $scope.disponibilidad = null;

    $scope.verificarDisponibilidad = function() {
        if ($scope.reserva.fecha_reserva && $scope.reserva.hora_reserva && $scope.reserva.cantidad_personas) {
            $http.get('/api/disponibilidad/', {
                params: {
                    fecha: $scope.reserva.fecha_reserva,
                    hora: $scope.reserva.hora_reserva,
                    personas: $scope.reserva.cantidad_personas
                }
            }).then(function(response) {
                $scope.disponibilidad = response.data.disponible;
            });
        }
    };

    $scope.$watchGroup([
        'reserva.fecha_reserva',
        'reserva.hora_reserva',
        'reserva.cantidad_personas'
    ], $scope.verificarDisponibilidad);

});

app.controller('ConsultaController', function($scope, $http) {
    $http.get('/api/mesas_disponibles/?fecha=2025-12-31')
        .then(function(response) {
            $scope.mesas = response.data.mesas;
        });
});
