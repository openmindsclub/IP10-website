<template>
    <div id="activities" class="hero">

        <b-container fluid class="page">
            <b-row>
                <b-col lg="3" md="4" sm="12">
                    <div class="battle-graphic">
                        <Paragraph title="Battle Graphique" content="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."/>
                    </div>
                </b-col>
            </b-row>
            <b-row>
                <b-col lg="8" md="7" sm="0">
                    <div class="void"></div>
                </b-col>
                <b-col lg="3" md="4" sm="12">
                    <div class="tresor-hunt">
                        <Paragraph title="Chasse au Tresor" content="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."/>
                    </div>
                </b-col>
            </b-row>
        </b-container>



    </div>
</template>

<script>
import Paragraph from '../components/Paragraph.vue'
export default {
    name: "Activities",
    components: {
        Paragraph
    },
};
</script>


<style scoped >
.hero{
    background-image: url("../assets/backgrounds/activities_background.jpg");

    height: 100vh;
    width: 100%;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;

    display: flex;
    flex-direction: column;
}

.page{
    padding-left: 10%;
    padding-top:8%;
    padding-right: 3%;
}
</style>
