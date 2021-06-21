<template>
  <div id="sponsor" class="about">
    <h2>Meet our Sponsor</h2>

    <b-container fluid class="page">
        <b-row class="row-class" align-v="center" align-h="center">
            <b-col class="logo" md="2" sm="4">
                <b-img center :src="require(`../assets/${sponsorLogo}`)" fluid v-bind:alt="sponsorName"></b-img>
            </b-col>
            <b-col md="8" sm="10">
                <Paragraph :title="sponsorName" :content="sponsorDescription"/>
            </b-col>
        </b-row>
    </b-container>

    <b-container fluid class="page">
        <b-row class="row-class" align-v="center" align-h="around">
            <b-col col="3" md="2" xl="1">
                <b-img center :src="require(`../assets/go.png`)" fluid alt="global opurtunities logo"></b-img>
            </b-col>
            <b-col col="3" md="2" xl="1">
                <b-img center :src="require(`../assets/usthb_logo.png`)" fluid alt="usthb logo"></b-img>
            </b-col>
            <b-col col="3" md="2" xl="1" >
                <b-img center :src="require(`../assets/sdacs.png`)" fluid alt="sdacs logo"></b-img>
            </b-col>
        </b-row>
    </b-container>
  </div>
</template>

<script>
import Paragraph from '../components/Paragraph.vue';
export default {
    name: "Sponsor",
    components: {
        Paragraph
    },
    data: () => ({
        sponsorName: "Stark Industries",
        sponsorLogo: "Stark_ind.png",
        sponsorDescription: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    }),
};
</script>

<style scoped >
.about{
    background-image: url("../assets/backgrounds/sponsor.png");

    height: 100vh;
    width: 100%;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;

    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;

    padding-bottom: 50px;
}

h2{
    color: white;
    font-size: 70px;
    margin-top: 60px;
    margin-bottom: 30px;
}

@media(max-width: 765px){

    .about {
        height: fit-content;
        background-repeat: repeat;
    }

    .row-class{
        width: 100%;
    }

    h2{
        font-size: 50px;
    }
}


</style>
