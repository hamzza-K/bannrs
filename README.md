Colored terminal banners for information.

`from banners import Banner`

```
ban = Banner(style='+')
ban.success('The following request was a success!')
```

![image](https://user-images.githubusercontent.com/34022534/221373810-bf884504-2828-4d36-8dee-d5c77fba9fde.png)

```
ban = Banner(style='*')
ban.error('Unauthorised request!')
```
![image](https://user-images.githubusercontent.com/34022534/221373968-a0862c1e-3cff-430c-94db-a39b9fb8955e.png)

```
ban = Banner()
ban.info('Object was found. Searching further...')
```
![image](https://user-images.githubusercontent.com/34022534/221374037-15008c9b-ca0d-403a-b239-a6cea4716cbb.png)
