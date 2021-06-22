<template>
<header>
	<nav>
		<div class="logo-box">
			<router-link :to="items[0].path"><img class="logo"  src="../assets/logoIP10.png"/></router-link>
		</div>
    	<div class="menu-icon">
        	<i class="fa fa-bars fa-2x" @click="toogleSlideBar()"></i>
        </div>
        <div class="menu">
        	<ul v-bind:class="{showing: sidebar}" :class="backgroundTheme">
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
	props: ['route'],
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
			{ title: "Sponsor", route:false, composed: false, path: "Home#sponsor"},
		]
	}),
	methods: {
		toogleSlideBar(){
			this.sidebar = !this.sidebar
		}
	},
	computed: {
		backgroundTheme() {
			if (this.route == "welcome"){
				return "welcome-background"
			} else if (this.route == "home") {
				return "home-background"
			} else if (this.route == "registration") {
				return "registration-background"
			}
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
    line-height: 30px;
    z-index: 99999999;

}

.logo{
	width: 35px;
	position: fixed;
	margin-left: 15px;
	margin-top: 13px;
}

nav ul {
    line-height: 35px;
    list-style: none;
    overflow: hidden;
    text-align: right;
}

nav ul li {
    display: inline-block;
    padding: 10px 30px;
}

nav ul li a {
    font-size: 20px;
}

nav ul li .dropbtn {
    color: #4B535C;
	background: rgba(0, 0, 0, 0);
    font-size: 20px;
	border: none;
  	outline: none;
}

nav ul li a:hover{
    color: #E1CF4B;
}

.dropdown {
  display: inline-block;
}

/* Dropdown Content (Hidden by Default) */
.dropdown-content {
  display: none;
  position: fixed;
  padding: 20px;
  z-index: 99999;
}

/* Links inside the dropdown */
.dropdown-content a {
  display: block;
  text-align: left;
  padding-top: 10px;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropdown-content {
	display: block;
}

/* Show the dropdown menu on hover */
.dropdown:hover .dropbtn {
	color: #E1CF4B;
}

.menu-icon {
    line-height: 45px;
    width: 100%;
    background: none;
    box-sizing: border-box;
    padding: 10px 30px;
    cursor: pointer;
    color: #fff;
    display: none;
}

@media(max-width: 725px) {

	.logo{
		position: absolute;
		right: 0px;
		margin-left: 0px;
		margin-right: 15px;
	}

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

/* welcome screen */
.welcome-background{
	background: #F2F5FE;
}

.welcome-background a{
    color: #4B535C;
}

.welcome-background .dropbtn{
    color: #4B535C;
}

.welcome-background .dropdown-content {
  background: #F2F5FE;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
}


/* home screen */
.home-background{
	background: #41494C;
}

.home-background a{
    color: white;
}

.home-background .dropbtn{
    color: white;
}

.home-background .dropdown-content {
  background: #41494C;
}


/* registration screen */
.registration-background{
	background: rgba(0, 0, 0, 0);
}

.registration-background a{
    color: white;
}

.registration-background .dropbtn{
    color: white;
}

.registration-background .dropdown-content {
  background: #41494C;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
}

</style>
