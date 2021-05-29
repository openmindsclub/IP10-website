<template>
    <div id="home">
		<!-- Navigation -->
		<div id="navbar" class="navbar navbar-expand-md navbar-dark fixed-top">
			<a class="navbar-brand" href="/">
			<img src="src/assets/logo.png" width="40px" class="img-fluid" alt="Logo">
			</a>
			<button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarResponsive">
				<span class="navbar-toggler-icon"></span>
			</button>

			<div class="collapse navbar-collapse" id="navbarResponsive">
				<ul class="navbar-nav ml-auto">
                
					<li class="nav-item" v-for="item in items" :key="item.title">
                        <a class="nav-link" :href="item.path">{{ item.title }}</a>
                    </li>
					
				</ul>
			</div>
		</div>
	</div>

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
			{ title: "A Propos", path: "/#/apropos"},
		]
	}),
};
</script>
