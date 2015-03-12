/**
 * Created by robert on 12/03/15.
 */

// create the controller and inject Angular's $scope
wepredictApp.controller('mainController',['myService','$scope','$route', '$window', '$location','dataFactory',
    function(myService,$scope,$route, $window, $location,dataFactory) {

        $scope.labels = ["January", "February", "March", "April", "May", "June", "July"];
        $scope.series = ['Series A', 'Series B'];
        $scope.data = [
            [65, 59, 80, 81, 56, 55, 40],
            [28, 48, 40, 19, 86, 27, 90]
        ];
        $scope.onClick = function (points, evt) {
            console.log(points, evt);
        };
        $scope.message = 'Everyone come and see how good I look!';
        $scope.alert = function(id,desc){
            var obj = {name:id,dec:desc};
            myService.set(obj);
            console.log(id+" | "+desc);
            $location.path('ccg');
            $scope = $scope || angular.element(document).scope();
            $scope.$apply();
        };


        $scope.ccgSelected = {};
        $scope.update = function() {

            var obj = {dec:$scope.ccgSelected.CCG};
            myService.set(obj);
            $location.path('ccg');
            $scope = $scope || angular.element(document).scope();
            $scope.$apply();
        };

        dataFactory.getCCG()
            .success(function (data) {
                $scope.ccg = data;
                $scope.ccgSelected = $scope.ccg[0];
            })
            .error(function (error) {
                $scope.message = 'Unable to load customer data: ' + error.message;
            });


    }]);