<template>
  <div class="my-auto">
    <section class="home-carousel">
      <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
        <div class="carousel-inner">
          <div class="carousel-item active">
            <img class="d-block w-100" src="https://api.time.com/wp-content/uploads/2020/03/stock-market-coronavirus-2.jpg" alt="First slide">
          </div>
        </div>
      </div>
    </section>
  
    <section class="container icons-carousel">
      <h2 class="my-4">Sonos: Predict your Favorite Stock</h2>
      <h4 class="my-c-25">Our Current Top Pick</h4>
      <div class="d-flex justify-content-around flex-wrap">
        <HomeCard symbol="GOOGL" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/368px-Google_2015_logo.svg.png"/>
        <HomeCard symbol="AAPL" src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Apple_logo_black.svg/80px-Apple_logo_black.svg.png"/>
        <HomeCard symbol="AMZN" src= "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Amazon_logo.svg/175px-Amazon_logo.svg.png"/>
      </div>
   </section>

   <footer class="py-2 bg-dark">
    <div class="container">
      <p class="m-0 text-center text-white">Sonos Project &copy; 2020</p>
    </div>
    <!-- /.container -->
  </footer>
  </div>
</template>

<script>
import HomeCard from '@/components/HomeCard'

export default {
  name: 'Home',
  components: {
    HomeCard
  }
}
</script>

<style scoped>
  footer {
    margin-top: 2%;
  }
  img {
    float: left;
    width:  100px;
    height: 300px;
    object-fit: cover;
  }
</style>
