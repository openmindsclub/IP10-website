<template>
    <div id="event" class="hero">
        <div class="space"></div>
        <b-container fluid class="page">
            <b-row class="row-class" align-v="center" align-h="center">
                <b-col class="leftside" md="6" sm="12">
                    <h2>Tout sur L'Install Party</h2>
                    <img class="large_white_line"  src="../assets/large_white_line.png"/>
                    <p>
                        Après deux ans d'absence, suite à des circonstances indépendantes de notre volonté, notre événement phare "L'Install Party" revient le 12 juillets 2021 pour une 10éme édition avec comme thème "New Era" !!

                    </p>
                    <p>
                        L'Install party c’est un événement autours de l’open source, le libre et l’esprit de partage de manière générale destrier aux passionnés du domaine, autant aux experts qu’aux débutants. Durant toute la journée nous proposerons des conférences, workshops mais aussi plein d'autres activités et bien sure comme chaque édition, l’essence de l’événement, à savoir vous offrir l'installation de distributions Linux !

                    </p>
                </b-col>
                <b-col class="rightside" md="6" sm="12">
                    <div class="">
                        <b-row align-h="center" align-v="center">
                            <b-col md="7">
                                <div>
                                    <b-img center :src="require('../assets/logoIP10_edition.png')" fluid alt="Responsive image" class="IPlogo"></b-img>
                                </div>
                            </b-col>
                        </b-row>
                    </div>
                </b-col>
            </b-row>
        </b-container>
    </div>
</template>

<script>
export default {
  name: "Event",
};
</script>


<style scoped >
.hero{
    background-image: url("../assets/backgrounds/Event_background_1.jpg");

    height: 100vh;
    width: 100%;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;
}

.space{
    height: 15%;
}

.page{
    padding-left: 3%;
}

.margin-row{
    margin-left: 0;
    margin-right: 0;
}

.leftside{
    padding-right: 10%;
}

.leftside h2{
    font-size: 3em;
    color: white;
}

.leftside img{
    width:90%;
}

.leftside p{
    color: white;
    font-size: 20px;
}

.rightside .clubLogo{
    width:100%;
}

.rightside .IPlogo{
    width:100%;
    margin-top: 5%;
}


@media(max-width: 1300px){
    .leftside h2{
        font-size: 2em;
    }

    .leftside p{
        font-size: 16px;
    }
}

@media(max-width: 900px){
    .leftside p{
        font-size: 13px;
    }
}

@media(max-width: 770px){

    .hero {
        height: fit-content;
    }

    .space{
        height: 80px;
    }

    .leftside{
        padding-right: 10px;
    }

    .leftside h2{
        font-size: 30px;
    }

    .leftside p{
        font-size: 14px;
    }

    .rightside .clubLogo{
        display: none;
    }

    .rightside .IPlogo{
        width:60%;
        margin-top: 15px;
        margin-bottom: 40px;
    }
}

</style>
