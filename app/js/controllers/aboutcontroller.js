/**
 * Created by robert on 12/03/15.
 */
wepredictApp.controller('aboutController', ['myService','$scope', function(myService,$scope) {
    var obj = myService.get();
    $scope.message = 'About This Site';
}]);