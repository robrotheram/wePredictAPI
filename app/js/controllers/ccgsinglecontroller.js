wepredictApp.controller('ccgController', ['myService','dataFactory','$scope','$location','$timeout', function(myService,dataFactory,$scope,$location,$timeout) {
    var obj = myService.get();
    $scope.ccgid = obj.name;
    $scope.ccgname = obj.dec;
    $scope.message = obj.dec;

    $scope.ccgdata = [
        [11975,  5871, 8916, 2868],
        [ 1951, 10048, 2060, 6171],
        [ 8010, 16145, 8090, 8045],
        [ 1013,   990,  940, 6907]
    ];

    $scope.practiceSelected = {}

    dataFactory.getPracticeList(obj.dec)
        .success(function (data) {
            $scope.practice = data;
            $scope.practiceSelected = $scope.practice[0];
        })
        .error(function (error) {
            $scope.message = 'Unable to load customer data: ' + error.message;
        });



    $scope.update = function() {
        $timeout(function() {
            var obj = {prac: $scope.practiceSelected.Practice, dec: $scope.ccgname};
            myService.set(obj);
            $location.path('practice');
            $scope = $scope || angular.element(document).scope();
            $scope.$apply();
        });
    };


}]);


