wepredictApp.controller('contactController', ['$scope', 'dataFactory',
    function ($scope, dataFactory) {



        dataFactory.getAsthma()
            .success(function (custs) {
                $scope.message = custs.data[0][0];
            })
            .error(function (error) {
                $scope.message = 'Unable to load customer data: ' + error.message;
            });


    }]);