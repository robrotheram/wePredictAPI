/**
 * Created by robert on 12/03/15.
 */

wepredictApp.directive( 'ccgPoly', ['$location',
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
                    var topo;



                    topo = $.grep(countries, function(e){ return (e.properties.description).toLowerCase() == (scope.ccgid).toLowerCase(); });

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
