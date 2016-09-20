var game = new Phaser.Game(800, 800, Phaser.AUTO, 'game', { preload: preload, create: create, render:render });

function preload () {

    game.load.image('logo', 'img/phaser.png');

}

function create () {

    var logo = game.add.sprite(game.world.centerX, game.world.centerY, 'logo');
    logo.anchor.setTo(0.5, 0.5);

}

function render () {

            
}
