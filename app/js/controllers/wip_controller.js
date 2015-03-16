wepredictApp.controller('contactController', ['$scope', 'dataFactory',
    function ($scope, dataFactory) {



        dataFactory.getAsthma()
            .success(function (custs) {
                $scope.message = custs.data[0][0];
            })
            .error(function (error) {
                $scope.message = 'Unable to load customer data: ' + error.message;
            });

        $scope.ccgdata = [
            [11975,  5871, 8916, 2868],
            [ 1951, 10048, 2060, 6171],
            [ 8010, 16145, 8090, 8045],
            [ 1013,   990,  940, 6907]
        ];

    }]);