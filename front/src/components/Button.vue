<template>
<!-- au lien de v-on on peut mettre @ donc on peut metter @click-->
<button v-on:click="onClick()" :style="{background: color}" class="btn">{{text}}</button>
</template>
<script>

export default {
    name: 'Button',
    props: {
        text: String,
        color: String
    },
    methods: {
        onClick(){
            console.log("clicked")}
    },

}
</script>
<style scoped>
</style>