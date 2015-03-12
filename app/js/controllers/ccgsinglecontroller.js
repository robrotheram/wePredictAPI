wepredictApp.controller('ccgController', ['myService','$scope', function(myService,$scope) {
    var obj = myService.get();
    $scope.ccgid = obj.name;
    $scope.ccgname = obj.dec;
    $scope.message = obj.dec;
}]);


