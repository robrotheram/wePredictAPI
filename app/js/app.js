/**
 * Created by robert on 09/03/15.
 */

var scotchApp = angular.module('scotchApp', ['ngRoute','angularChart','chart.js']);

scotchApp.factory('myService', function() {
    var savedData = {}
    function set(data) {
        savedData = data;
    }
    function get() {
        return savedData;
    }

    return {
        set: set,
        get: get
    }

});


scotchApp.factory('dataFactory', ['$http', function($http) {

        var urlBase = 'http://wepredict.robrotheram.com/v1/';
        var dataFactory = {};

        dataFactory.getAsthma = function () {
            return $http.get(urlBase+'/getasmtha?limit=5');
        };

    /*
        dataFactory.getCustomer = function (id) {
            return $http.get(urlBase + '/' + id);
        };

        dataFactory.insertCustomer = function (cust) {
            return $http.post(urlBase, cust);
        };

        dataFactory.updateCustomer = function (cust) {
            return $http.put(urlBase + '/' + cust.ID, cust)
        };

        dataFactory.deleteCustomer = function (id) {
            return $http.delete(urlBase + '/' + id);
        };

        dataFactory.getOrders = function (id) {
            return $http.get(urlBase + '/' + id + '/orders');
        };
*/
        return dataFactory;
    }]);


// configure our routes
scotchApp.config(function($routeProvider,$locationProvider) {


    $routeProvider

        // route for the home page
        .when('/', {
            templateUrl : 'views/home.html',
            controller  : 'mainController'
        })

        // route for the about page
        .when('/about', {
            templateUrl : 'views/about.html',
            controller  : 'aboutController'
        })

        // route for the contact page
        .when('/contact', {
            templateUrl : 'views/contact.html',
            controller  : 'contactController'
        })
        // route for the contact page
        .when('/ccg', {
            templateUrl : 'views/ccgName.html',
            controller  : 'ccgController'
        });
});

scotchApp.directive( 'ccgMap', ['$location',
    function ($location) {
        return {
            restrict: 'E',
            scope: {

                data: '=',
                callbackFn:'&'
            },
            link: function (scope, element) {

                d3.select(window).on("resize", throttle);
                var scaleValue = 0;
                var zoom = d3.behavior.zoom()
                    .scaleExtent([1, 9])
                    .on("zoom", move);
                var width = $('#ccgMap').width();
                var projection;
                var height = (width )*1;
                var topo,projection,path,svg,g;
                var scaleValue = 4000;
                if($(document).width()>1500){
                    var scaleValue = 5500;
                }
                if($(document).width()<1500){
                    var scaleValue = 3000;
                }
                if($(document).width()<1200){
                    var scaleValue = 1900;
                }
                if($(document).width()<750){
                    var scaleValue = 1000;
                }
                $("#CCGData").hide();
                setup(width,height);

                d3.json("js/ccg.json", function(error, world) {

                    var countries = topojson.feature(world, world.objects.CCG).features;

                    topo = countries;
                    draw(scope,topo);


                    /* ******************* END *********************************** */


                });


                function draw (scope,topo) {
                    var country = g.selectAll(".country").data(topo);
                    console.log(country.enter());

                        country.enter().insert("path")
                            .attr("class", "country")
                            .attr("d", path)
                            .attr("id", function (d, i) {
                                return d.id;
                            })
                            .attr("title", function (d, i) {
                                return d.properties.name;
                            })
                            .style("fill", function (d) {
                                var randomColor = "#000000".replace(/0/g, function () {
                                    return (~~(Math.random() * 16)).toString(16);
                                });
                                return randomColor;
                            });

                        country
                            .on("load",function (d, i) {
                                alert(d);
                            })
                            .on("mousemove", function (d, i) {
                                var mouse = d3.mouse(svg.node()).map(function (d) {
                                    return parseInt(d);
                                });
                                $("#CCGData").show();
                                $("#CCGData").html(d.properties.description);
                            })
                            .on("mouseout", function (d, i) {
                                $("#CCGData").hide();
                            })
                            .on("dblclick", function (d, i) {

                                scope.callbackFn({id: d.properties.name, desc: d.properties.description});
                            });
                    //}
                }

                function setup(width,height){
                    projection = d3.geo.mercator()
                        .center([-2, 53])
                        .scale(scaleValue)
                        .translate([width / 2, height / 2]);

                    path = d3.geo.path().projection(projection);

                    svg = d3.select(element[0]).append("svg")
                        .attr("width", width)
                        .attr("height", height)
                        .call(zoom)
                        //.on("click", click)
                        .append("g");
                    g = svg.append("g");
                }

                function redraw() {
                    width =  element[0].width();
                    height = (width / 4)*3;
                    d3.select('svg').remove();
                    setup(width,height);
                    draw(topo);
                }


                function move() {

                    var t = d3.event.translate;
                    var s = d3.event.scale;
                    zscale = s;
                    var h = height/4;


                    zoom.translate(t);


                    zoom.translate(t);
                    g.attr("transform", "translate(" + t + ")scale(" + s + ")");

                    //adjust the country hover stroke width based on zoom level
                    d3.selectAll(".country").style("stroke-width", 1.5 / s);

                    console.log(t);

                }



                var throttleTimer;
                function throttle() {
                    window.clearTimeout(throttleTimer);
                    throttleTimer = window.setTimeout(function() {
                        redraw();
                    }, 200);
                }
            }}}
]);


scotchApp.directive( 'ccgPoly', ['$location',
    function ($location) {
        return {
            restrict: 'E',
            scope: {

                data: '=',
                callbackFn:'&',
                ccgid:'='
            },
            link: function (scope, element) {
                d3.select(window).on("resize", throttle);
                var scaleValue = 0;
                var width = element.parent()[0].offsetWidth;
                var projection;
                var height = width / 2;
                var topo,projection,path,svg,g;
                var scaleValue = 4000;
                if($(document).width()<2000){
                    var scaleValue = 25000;
                }
                if($(document).width()<1200){
                    var scaleValue = 1900;
                }
                if($(document).width()<750){
                    var scaleValue = 1000;
                }
                $("#CCGData").hide();
                setup(width,height);
                d3.json("js/ccg.json", function(error, world) {

                    var countries = topojson.feature(world, world.objects.CCG).features;

                    topo = $.grep(countries, function(e){ return e.properties.name == scope.ccgid; });

                    var b = path.bounds(topo[0]),
                        s = .95 / Math.max((b[1][0] - b[0][0]) / width, (b[1][1] - b[0][1]) / height),
                        t = [(width - s * (b[1][0] + b[0][0])) / 2, (height - s * (b[1][1] + b[0][1])) / 2];
                    var proj  = d3.geo.albers()
                        .scale(s)
                        .translate(t);
                    console.log(s);
                    console.log(t);
                    path = d3.geo.path().projection(proj);
                    draw(scope,topo);


                    /* ******************* END *********************************** */


                });


                function draw (scope,topo) {
                    var country = g.selectAll(".ccg").data(topo);
                    console.log(country.enter());

                    country.enter().insert("path")
                        .attr("class", "ccg")
                        .attr("d", path)
                        .attr("id", function (d, i) {
                            return d.id;
                        })
                        .attr("title", function (d, i) {
                            return d.properties.name;
                        })
                        .style("fill", "#C3CE10");


                }

                function setup(width,height){
                    projection = d3.geo.albers()
                        .scale(1)
                        .translate([0,0]);

                    path = d3.geo.path().projection(projection);

                    svg = d3.select(element[0]).append("svg")
                        .attr("width", width)
                        .attr("height", height)
                        .append("g");
                    g = svg.append("g");
                }
                var throttleTimer;
                function throttle() {
                    window.clearTimeout(throttleTimer);
                    throttleTimer = window.setTimeout(function() {
                        redraw();
                    }, 200);
                }
            }}}
]);







// create the controller and inject Angular's $scope
scotchApp.controller('mainController',['myService','$scope','$route', '$window', '$location','$timeout',
    function(myService,$scope,$route, $window, $location,$timeout) {

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


}]);

scotchApp.controller('aboutController', ['myService','$scope', function(myService,$scope) {
    var obj = myService.get();
    $scope.message = 'Look! I am an about page.'+obj.dec;
}]);


scotchApp.controller('ccgController', ['myService','$scope', function(myService,$scope) {
    var obj = myService.get();
    $scope.ccgid = obj.name;
    $scope.ccgname = obj.dec;
    $scope.message = obj.dec;
}]);

scotchApp.controller('contactController', ['$scope', 'dataFactory',
    function ($scope, dataFactory) {

    dataFactory.getAsthma()
        .success(function (custs) {
            $scope.message = custs.data[0][0];
        })
        .error(function (error) {
            $scope.message = 'Unable to load customer data: ' + error.message;
        });

}]);
