/**
 * Created by robert on 12/03/15.
 */
wepredictApp.factory('dataFactory', ['$http', function($http) {

    var urlBase = 'http://wepredict.robrotheram.com/v1/';
    var dataFactory = {};

    dataFactory.getAsthma = function () {
        return $http.get(urlBase+'/getasmtha?limit=5');
    };

    dataFactory.getCCG = function () {
        return $http.get(urlBase+'/getccg');
    };

    dataFactory.getPracticeList = function (practice) {
        return $http.get(urlBase+'/getpractice?practice='+encodeURIComponent(practice));
    };

    return dataFactory;


}]);
