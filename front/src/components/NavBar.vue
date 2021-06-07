<template>
<header>
	<nav>
    	<div class="menu-icon" @click="toogleSlideBar()">
        	<i class="fa fa-bars fa-2x"></i>
        </div>
        <div class="menu">
        	<ul v-bind:class="{showing: sidebar}">>
				<li v-for="item in items" :key="item.title">
					<a :href="item.path">{{ item.title }}</a>
				</li>
            </ul>
        </div>
    </nav>
</header>
</template>

<script>
export default {
	data: () => ({
		sidebar: false,
		items: [
			{ title: "Acceuil", path: "/#/acceuil"},
			{ title: "Event", path: "/#/event"},
			{ title: "Planning", path: "/#/planning"},
			{ title: "Sponsor", path: "/#/sponsor"},
			{ title: "A propos", path: "/#/apropos"},
		]
	}),
	methods: {
		toogleSlideBar(){
			this.sidebar = !this.sidebar
		}
	}
};

</script>


<style scoped>

header {
    width: 100%;
}

nav {
    position: fixed;
    width: 100%;
    line-height: 60px;
    z-index: 99999999;
}

nav ul {
    line-height: 45px;
    list-style: none;
    background: rgba(0, 0, 0, 0);
    overflow: hidden;
    color: #fff;
    padding: 0;
    text-align: center;
    margin: 0;
    transition: 1s;
}

nav ul {
    line-height: 45px;
    list-style: none;
    background: rgba(0, 0, 0, 0);
    overflow: hidden;
    color: #fff;
    padding: 0;
    text-align: right;
    margin: 0;
    transition: 1s;
}

nav ul li {
    display: inline-block;
    padding: 10px 40px;;
}

nav ul li a {
    font-family: 'Bungee', cursive;
    text-decoration: none !important;
    color: #000;
    font-size: 18px;
}

nav ul li a:hover{
    color: rgb(231, 22, 57);
}

.menu-icon {
    line-height: 45px;
    width: 100%;
    background: #000;
    text-align: right;
    box-sizing: border-box;
    padding: 10px 30px;
    cursor: pointer;
    color: #fff;
    display: none;
}

@media(max-width: 725px) {
    nav ul {
          max-height: 0px;
          background: #000;
    }

    .showing {
          max-height: 34em;
    }

    nav ul li {
          box-sizing: border-box;
          width: 100%;
          padding: 24px;
          text-align: center;
    }
    nav ul li a {
        font-family: 'Bungee', cursive;
        text-decoration: none !important;
        color: #fff;
        font-size: 18px;
    }
    nav ul li a:hover{
        color: rgb(231, 22, 57);
    }

    .menu-icon {
          display: block;
    }

}
</style>
