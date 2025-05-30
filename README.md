# 🛍️ MyShop - Application de Gestion de Stock Hors-ligne

**MyShop** est une application mobile de gestion de stock conçue pour les vendeurs individuels. Elle fonctionne entièrement **hors-ligne**, avec une interface intuitive et une protection par licence locale.

---

## 📱 Fonctionnalités Principales

### 🧭 Navigation
- Menu de navigation en bas (BottomNavigationBar)
- 4 pages principales :
  - **Accueil** : Vue d'ensemble rapide
  - **Inventaire** : Ajout, modification et suppression des produits
  - **Statistiques** : Graphiques simples de performance
  - **Abonnement** : Activation et vérification de licence

### 🖥️ Accueil
- Nombre total d’articles
- Revenu total estimé
- Produits les plus vendus

### 📦 Inventaire
Chaque article contient :
- Nom
- Catégorie
- Quantité
- Prix d’achat
- Prix de vente
- Image (optionnelle)

> Stock mis à jour automatiquement après vente ou achat

### 📊 Statistiques
- Graphiques hebdomadaires/mensuels des ventes
- Produits les plus vendus
- Revenus générés

### 📄 Reçu (affiché à l’écran uniquement)
- Nom du produit
- Quantité
- Prix unitaire
- Total
- Date et heure

---

## 🔐 Système de Licence

- Génère l’Android ID au premier démarrage
- Période d’essai : **7 jours**
- Après expiration, seul l’écran d’abonnement est accessible
- Licence chiffrée et fournie par l’administrateur à partir de :
  - Android ID
  - Date de début
  - Date de fin
- Vérification locale, aucune connexion Internet requise

---

## 📁 Structure du Projet

