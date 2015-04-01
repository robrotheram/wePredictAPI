/**
 * Created by robert on 12/03/15.
 */
wepredictApp.directive( 'ccgMap', ['$location',
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
                // $("#CCGData").hide();
                setup(width,height);

                var tooltip = d3.select("#container").append("div").attr("class", "tooltip hidden");


                //              var offsetL = document.getElementById('container').offsetLeft+20;
//                var offsetT = document.getElementById('container').offsetTop+10;

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
                            tooltip.classed("hidden", true);
                        })
                        .on("mouseout", function (d, i) {
                            // $("#CCGData").hide();
                            tooltip.classed("hidden", true);
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

                    //console.log(t);

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