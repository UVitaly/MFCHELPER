<!DOCTYPE html>
<html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
        <link rel="stylesheet" href="css/main.css">
        <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,700;1,700&display=swap" rel="stylesheet"> 
        <link href = "https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel = "stylesheet">
	    <link href="http://fonts.googleapis.com/css?family=Open+Sans:300,400,700' rel='stylesheet" type="text/css">
	    <script type="text/javascript" src="http://code.jquery.com/jquery-1.9.1.js"></script>
        <script type="text/javascript" src="js/jquery.immersive-slider.js"></script>
        <link href="css/immersive-slider.css" rel="stylesheet" type="text/css">
        <title>MFCHelper</title>
    </head>

    <body>

        <header>
            <img  src = "Images/tg.png" class = "logo" href = "#">
            <div class="nav-bar">
                <div class = "name">MFCHELPER</div>
	    	    <nav>
	    	    	<ul>
	    	    		<li><a href = "#">ABOUT PROJECT</a></li>
	    	    		<li><a href = "#">PERSONAL ACCAUNT</a></li>
	    	    		<li><a href = "#">TELEGRAM-BOT</a></li>
	    	    	</ul>
	    	    </nav>
            </div>
	    	<div class="clearfix"></div>
            <?php
                if($_COOKIE['user']!=''):
                ?>
                <div class = "forms_container">

                    <div class="log_reg"> 

                        <div class="dropDown">

                            <button class="mainMenuBtn"><?php echo trim($_COOKIE['user']) ?></button>
                            <div class="dropDown-menu dropdown-menu">

                                <a href="/out.php">Выйти</a>
                                <button type="button" class="btn btn-primary btn-lg" data-toggle="modal" data-target="#myModal">
                                       Личный кабинет
                                </button>
                                <!-- Кнопка запуска модального окна -->
                                  

                                    <div id="myModal" class="modal" tabindex="-1">
                                        <div class="modal-dialog">
                                            <div class="modal-content">
                                                <div class="modal-header">
                                                    <h5 class="modal-title">Подтверждение</h5>
                                                    <button type="button" class="close" data-dismiss="modal">×</button>                
                                                </div>
                                                <div class="modal-body">
                                                    <p>Вы хотите сохранить изменения в этом документе перед закрытием?</p>
                                                    <p class="text-secondary"><small>Если вы не сохраните, ваши изменения будут потеряны.</small></p>
                                                </div>
                                                <div class="modal-footer">
                                                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Закрыть</button>
                                                    <button type="button" class="btn btn-primary">Сохранить изменения</button>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                    	<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
                                    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
                                    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
                                    <script>
                                        $(document).ready(function(){
                                            $("#myModal").modal('show');
                                        });
                                    </script>

                            </div>

                        </div>

                    </div>  

                </div>
                <?php
                else:
                ?>
                <div class = "forms_container">
                    <div class="log_reg">
                    
                        <a href="login.html">Login</a>
                        <p></p>
                        <a href="registration.html">Registration</a>

                    </div>  
                </div>  
                <?php
                endif;
                 ?>
	    </header>

        <div class="main">
      <div class="page_container">
        <div id="immersive_slider">
          <div class="slide" data-blurred="img/slide1_blurred.jpg">
            <div class="content">
              <h2><a href="http://www.bucketlistly.com" target="_blank">BucketListly</a></h2>
              <p>It’s never been easier to watch YouTube on the big screen
              Send your favorite YouTube videos from your Android phone or tablet to TV with the touch of a button. It’s easy. No wires, no setup, no nothing. Find out more here.</p>
            </div>
            <div class="image">
              <a href="http://www.bucketlistly.com" target="_blank">
                <img src="img/1.jpg" alt="Slider 1">
              </a>
            </div>
          </div>
          <div class="slide" data-blurred="img/slide2_blurred.jpg">
            <div class="content">
              <h2><a href target="_blank">BucketListly Apps</a></h2>
              <p>It’s never been easier to watch YouTube on the big screen
              Send your favorite YouTube videos from your Android phone or tablet to TV with the touch of a button. It’s easy. No wires, no setup, no nothing. Find out more here.</p>
            </div>
            <div class="image">
             <a href target="_blank"> <img src="img/2.jpg" alt="Slider 1"></a>
            </div>
          </div>
          <div class="slide" data-blurred="img/slide3_blurred.jpg">
            <div class="content">
              <h2><a href target="_blank">The Pete Design</a></h2>
              <p>It’s never been easier to watch YouTube on the big screen
              Send your favorite YouTube videos from your Android phone or tablet to TV with the touch of a button. It’s easy. No wires, no setup, no nothing. Find out more here.</p>
            </div>
            <div class="image">
              <a href="http://www.thepetedesign.com" target="_blank"><img src="img/3.jpg" alt="Slider 1"></a>
            </div>
          </div>
			<div class="slide" data-blurred="img/slide3_blurred.jpg">
            <div class="content">
              <h2><a href target="_blank">The Pete Design</a></h2>
              <p>It’s never been easier to watch YouTube on the big screen
              Send your favorite YouTube videos from your Android phone or tablet to TV with the touch of a button. It’s easy. No wires, no setup, no nothing. Find out more here.</p>
            </div>
            <div class="image">
              <a href="http://www.thepetedesign.com" target="_blank"><img src="img/4.jpg" alt="Slider 1"></a>
            </div>
          </div>
			
          
          <a href="#" class="is-prev">&laquo;</a>
          <a href="#" class="is-next">&raquo;</a>
        </div>
      </div>
  	</div>
  	<div class="benefits">
      <div class="page_container">

  	  </div>
  	</div>
  	<script type="text/javascript">
  	  $(document).ready( function() {
  	    $("#immersive_slider").immersive_slider({
  	      container: ".main"
  	    });
  	  });

    </script>
    </body>
    
</html>