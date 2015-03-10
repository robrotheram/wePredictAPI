/**
 * Created by robert on 09/03/15.
 */

var scotchApp = angular.module('scotchApp', ['ngRoute']);

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
                var width = element.parent()[0].offsetWidth;
                var height = width / 2;
                var topo,projection,path,svg,g;
                var scaleValue = 4000;
                if($(document).width()<2000){
                    var scaleValue = 2500;
                }
                if($(document).width()<1200){
                    var scaleValue = 1900;
                }
                if($(document).width()<750){
                    var scaleValue = 1000;
                }
                $("#CCGData").hide();
                setup(width,height);


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

                d3.json("js/ccg.json", function(error, world) {

                    var countries = topojson.feature(world, world.objects.CCG).features;

                    topo = countries;
                    draw(scope,topo);

                });

                function draw (scope,topo) {
                    var country = g.selectAll(".country").data(topo);


                    country.enter().insert("path")
                        .attr("class", "country")
                        .attr("d", path)
                        .attr("id", function(d,i) { return d.id; })
                        .attr("title", function(d,i) { return d.properties.name; })
                        .style("fill",function(d) {
                            var randomColor = "#000000".replace(/0/g,function(){return (~~(Math.random()*16)).toString(16);});
                            return randomColor;
                        });

                    country
                        .on("mousemove", function(d,i) {
                            var mouse = d3.mouse(svg.node()).map( function(d) { return parseInt(d); } );
                            $("#CCGData").show();
                            $("#CCGData").html("CCG Name: "+d.properties.description);
                        })
                        .on("mouseout",  function(d,i) {
                            $("#CCGData").hide();
                        })
                        .on("click",  function(d,i) {

                            scope.callbackFn({id:d.properties.name,desc:d.properties.description});
                        });
                }


                function redraw() {
                    width =  element[0].width();
                    height = width / 2;
                    d3.select('svg').remove();
                    setup(width,height);
                    draw(topo);
                }


                function move() {

                    var t = d3.event.translate;
                    var s = d3.event.scale;
                    zscale = s;
                    var h = height/4;

                    t[0] = Math.min(width / 2 * (s - 1), Math.max(width / 2 * (1 - s), t[0]));
                    t[1] = Math.min(height / 2 * (s - 1) + h * s, Math.max(height / 2 * (1 - s) - h * s, t[1]));

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


// create the controller and inject Angular's $scope
scotchApp.controller('mainController',['myService','$scope','$route', '$window', '$location',
    function(myService,$scope,$route, $window, $location) {

    // create a message to display in our view
    $scope.message = 'Everyone come and see how good I look!';
    $scope.alert = function(id,desc){

        //this will mark the URL change

        var obj = {name:id,dec:desc};
        myService.set(obj);
        console.log(id+" | "+desc);
        $location.path('about'); //use $location.path(url).replace() if you want to replace the location instead

        $scope = $scope || angular.element(document).scope();
        $scope.$apply();
    };


}]);

scotchApp.controller('aboutController', ['myService','$scope', function(myService,$scope) {
    var obj = myService.get();
    $scope.message = 'Look! I am an about page.'+obj.dec;
}]);

scotchApp.controller('contactController', function($scope) {
    $scope.message = 'Contact us! JK. This is just a demo.';
});
