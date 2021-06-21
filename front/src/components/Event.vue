<template>
    <div id="event" class="hero">
        <div class="space"></div>
        <b-container fluid class="page">
            <b-row class="row-class" align-v="center" align-h="center">
                <b-col class="leftside" md="6" sm="12">
                    <h2>Tout sur L'Install Party</h2>
                    <img class="large_white_line"  src="../assets/large_white_line.png"/>
                    <p>
                        L'Install Party c'est des conférences des workshops mais plus important c'est un evenement sur l'esprit du libre et du partage !
                    </p>
                    <p>
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
                        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Cupiditate, pariatur, quos corrupti iusto nulla corporis dolore accusamus similique eligendi facilis est quo non inventore quibusdam culpa dolor incidunt ipsa debitis!
                    </p>
                </b-col>
                <b-col class="rightside" md="6" sm="12">
                    <div class="">
                        <b-row class="margin-row" align-h="center">
                            <b-col md="3">
                                <img class="clubLogo" src="../assets/omc_logo_white.png"/>
                            </b-col>
                            <b-col md="3">
                                <img class="clubLogo" src="../assets/omc_logo_white.png"/>
                            </b-col>
                            <b-col md="3">
                                <img class="clubLogo" src="../assets/omc_logo_white.png"/>
                            </b-col>
                        </b-row>
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
        overflow-y: scroll;
        -ms-overflow-style: none;  /* Hide scrollbar for IE and Edge */
        scrollbar-width: none;
    }

    /* Hide scrollbar for Chrome, Safari and Opera */
    .hero::-webkit-scrollbar {
      display: none;
    }

    .space{
        height: 5%;
    }

    .leftside h2{
        font-size: 20px;
    }

    .leftside p{
        font-size: 13px;
    }

    .rightside .clubLogo{
        display: none;
    }

    .rightside .IPlogo{
        width:50%;
        margin-top: 10%;
        margin-bottom: 10%;
    }

    .row-class{
        width: 100%;
    }
}

</style>
