<template>
<header>
	<nav>
    	<div class="menu-icon" @click="toogleSlideBar()">
        	<i class="fa fa-bars fa-2x"></i>
        </div>
        <div class="menu">
        	<ul v-bind:class="{showing: sidebar}">
				<li v-for="item in items" :key="item.title">
					<router-link v-if= "item.route" :to="item.path">{{ item.title }}</router-link>
					<div v-else>
						<a v-if= "!item.composed" :href="item.path">{{ item.title }}</a>
						<div v-else class="dropdown">
							<button class="dropbtn">{{item.title}}
	      						<i class="fa fa-caret-down"></i>
	    					</button>
	  						<div class="dropdown-content">
								<a  v-for="subItem in item.components" :key="subItem.title" :href="subItem.path">{{ subItem.title }}</a>
	  						</div>
						</div>
					</div>
				</li>
            </ul>
        </div>
    </nav>
</header>
</template>

<script>
export default {
	name: "NavBar",
	data: () => ({
		sidebar: false,
		items: [
			{ title: "Acceuil", route:true, path: "/", composed: false},
			{ title: "Home", route:true, path: "Home", composed: false},
			{ title: "Activities", route:false, composed: true, components:[
				{ title: "Conferances", path: "Home#conferences"},
				{ title: "Workshops", path: "Home#workshops"},
				{ title: "Other Activities", path: "Home#activities"},
				{ title: "Stands", path: "Home#stands"}
			]},
			{ title: "Inscriptions", route:true, path: "Registration", composed: false},
			{ title: "A propos", route:false, composed: true, components:[
				{ title: "A propos", path: "/#/about"},
			]},
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
    color: #4B535C;
    padding: 0;
    text-align: right;
    margin: 0;
}

nav ul li {
    display: inline-block;
    padding: 10px 40px;;
}

nav ul li a {
    font-family: 'Bungee', cursive;
    text-decoration: none !important;
    color: #4B535C;
    font-size: 18px;
}

nav ul li .dropbtn {
    font-family: 'Bungee', cursive;
    text-decoration: none !important;
    color: #4B535C;
	background: rgba(0, 0, 0, 0);
    font-size: 18px;
	border: none;
  	outline: none;
	margin: 0;
}

nav ul li a:hover{
    color: #E1CF4B;
}

/* Dropdown Button */
.dropbtn {
  border: none;
}

/* The container <div> - needed to position the dropdown content */
.dropdown {
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  color: #F2F5FE;
  position: fixed;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  padding: 12px;
  z-index: 99999;
}

/* Links inside the dropdown */
.dropdown-content a {
  text-decoration: none;
  display: block;
  text-align: left;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
	display: block;
}

.menu-icon {
    line-height: 45px;
    width: 100%;
    background: none;
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
